import json
import os
import pickle
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import List, Literal, Optional


class FaceRecognitionError(Exception):
    """Base exception for face recognition failures."""


class FaceRecognitionUnavailable(FaceRecognitionError):
    """Raised when model files or ML dependencies are unavailable."""


class InvalidImageError(FaceRecognitionError):
    """Raised when uploaded bytes cannot be decoded as an image."""


@dataclass
class RecognizedFace:
    face_index: int
    nim: Optional[str]
    confidence: float
    detection_confidence: Optional[float]
    bbox: Optional[List[float]]


class FaceRecognitionService:
    """Recognize student NIM labels from uploaded face photos."""

    def __init__(self, model_dir: str, method: str, threshold: float):
        self.model_dir = Path(model_dir)
        self.method = method
        self.threshold = threshold
        self._classifier = None
        self._label_encoder = None
        self._detector = None
        self._embedder = None
        self._device = None

    def recognize(
        self,
        image_bytes: bytes,
        mode: Literal["single", "multi"] = "single",
    ) -> List[RecognizedFace]:
        """Return recognized faces from an uploaded image."""
        self._load_classifier()
        image = self._read_image(image_bytes)
        self._load_embedding_pipeline()

        boxes, _ = self._detector.detect(image)
        faces, detection_probs = self._detector(image, return_prob=True)

        if faces is None:
            return []

        if faces.ndim == 3:
            faces = faces.unsqueeze(0)

        if mode == "single" and faces.shape[0] > 1:
            faces = faces[:1]
            detection_probs = detection_probs[:1] if detection_probs is not None else None
            boxes = boxes[:1] if boxes is not None else None

        embeddings = self._create_embeddings(faces)
        predicted_classes = self._classifier.predict(embeddings)
        probabilities = self._classifier.predict_proba(embeddings)
        labels = self._label_encoder.inverse_transform(predicted_classes)

        results: List[RecognizedFace] = []
        for index, (label, class_id, row) in enumerate(
            zip(labels, predicted_classes, probabilities)
        ):
            confidence = float(row[list(self._classifier.classes_).index(class_id)])
            detection_confidence = None
            if detection_probs is not None and index < len(detection_probs):
                detection_confidence = float(detection_probs[index])

            bbox = None
            if boxes is not None and index < len(boxes):
                bbox = [float(value) for value in boxes[index]]

            nim = str(label) if confidence >= self.threshold else None
            results.append(
                RecognizedFace(
                    face_index=index,
                    nim=nim,
                    confidence=confidence,
                    detection_confidence=detection_confidence,
                    bbox=bbox,
                )
            )

        return results

    def _load_classifier(self) -> None:
        if self._classifier is not None and self._label_encoder is not None:
            return

        info_path = self.model_dir / "model_info.json"
        if info_path.exists():
            with info_path.open("r", encoding="utf-8") as file:
                model_info = json.load(file)
            self.method = model_info.get("best_method", self.method) or self.method

        classifier_path = self.model_dir / f"clf_{self.method}.pkl"
        label_encoder_path = self.model_dir / f"le_{self.method}.pkl"

        if not classifier_path.exists() or not label_encoder_path.exists():
            raise FaceRecognitionUnavailable(
                f"Model {self.method!r} tidak ditemukan di {self.model_dir}"
            )

        with classifier_path.open("rb") as file:
            self._classifier = pickle.load(file)

        with label_encoder_path.open("rb") as file:
            self._label_encoder = pickle.load(file)

        if getattr(self._classifier, "n_features_in_", None) != 512:
            raise FaceRecognitionUnavailable(
                "Classifier wajah harus menerima embedding 512 dimensi"
            )

        if not hasattr(self._classifier, "predict_proba"):
            raise FaceRecognitionUnavailable("Classifier wajah tidak mendukung confidence")

    def _load_embedding_pipeline(self) -> None:
        if self._detector is not None and self._embedder is not None:
            return

        if not os.environ.get("TORCH_HOME"):
            torch_home = self.model_dir / ".torch"
            torch_home.mkdir(parents=True, exist_ok=True)
            os.environ["TORCH_HOME"] = str(torch_home)

        try:
            import torch
            from facenet_pytorch import InceptionResnetV1, MTCNN
        except ImportError as exc:
            raise FaceRecognitionUnavailable(
                "Dependency face recognition belum terinstall. "
                "Install requirements.txt yang sudah diperbarui."
            ) from exc

        self._device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self._detector = MTCNN(
            image_size=160,
            margin=0,
            keep_all=True,
            post_process=True,
            device=self._device,
        )
        self._embedder = InceptionResnetV1(pretrained="vggface2").eval().to(self._device)

    def _read_image(self, image_bytes: bytes):
        try:
            from PIL import Image
        except ImportError as exc:
            raise FaceRecognitionUnavailable("Dependency Pillow belum terinstall") from exc

        try:
            return Image.open(BytesIO(image_bytes)).convert("RGB")
        except Exception as exc:
            raise InvalidImageError("File upload bukan gambar yang valid") from exc

    def _create_embeddings(self, faces):
        try:
            import torch
        except ImportError as exc:
            raise FaceRecognitionUnavailable("Dependency torch belum terinstall") from exc

        with torch.no_grad():
            return self._embedder(faces.to(self._device)).detach().cpu().numpy()
