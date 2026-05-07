from app.models.dosen import Dosen
from app.models.user import User
from app.seeders.base import BaseSeeder


class DosenSeeder(BaseSeeder):
    """Seeder for dosen table - links users to dosen records."""
    
    def seed(self):
        # Get the dosen user from users table
        dosen_user = self.db.query(User).filter(User.email == "dosen@absenin.local").first()
        
        if not dosen_user:
            print("Warning: dosen@absenin.local user not found. Run UserSeeder first.")
            return
        
        # Check if dosen already exists
        exists = self.db.query(Dosen).filter(Dosen.id_user == dosen_user.id).first()
        if exists:
            self.skipped += 1
        else:
            dosen = Dosen(id_user=dosen_user.id)
            self.db.add(dosen)
            self.inserted += 1
        
        self.db.commit()
