# included in tutorial package
from sqlalchemy.future import select
from app.db.models import User

class UserRepository:

    @staticmethod
    async def get_by_email(db, email):
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db, user_data):
        user = User(**user_data)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user