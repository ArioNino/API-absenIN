from app.models.user import User
import bcrypt
from app.seeders.base import BaseSeeder


class UserSeeder(BaseSeeder):
    DATA = [
        ("dosen@absenin.local", "dosen123", "Dosen"),
    ]

    def seed(self):
        for email, password, name in self.DATA:
            exists = self.db.query(User).filter(User.email == email).first()
            
            # Hash password dengan bcrypt
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            if exists:
                # Update password jika sudah ada
                exists.password = hashed
                self.skipped += 1
            else:
                u = User(email=email, password=hashed, name=name)
                self.db.add(u)
                self.inserted += 1
        self.db.commit()
