# included in tutorial package
from app.repository.user_repo import UserRepository
from app.core.security import hash_password, verify_password, create_access_token

class UserService:

    @staticmethod
    async def register(db, user):
        existing = await UserRepository.get_by_email(db, user.email)
        if existing:
            return None

        user.password = hash_password(user.password[:72])
        return await UserRepository.create(db, user.dict())

    @staticmethod
    async def login(db, user):
        db_user = await UserRepository.get_by_email(db, user.email)

        if not db_user:
            return None

        if not verify_password(user.password[:72], db_user.password):
            return None

        return create_access_token({"sub": db_user.email})