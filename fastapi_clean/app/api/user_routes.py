# included in tutorial package
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.user_schema import UserCreate, UserLogin, UserOut
from app.services.user_service import UserService

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    created_user = await UserService.register(db, user)

    if not created_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    return created_user

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    token = await UserService.login(db, user)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token, "token_type": "bearer"}