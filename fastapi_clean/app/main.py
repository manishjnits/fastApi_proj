from fastapi import FastAPI
from app.api.user_routes import router
from app.db.database import engine, Base

app = FastAPI(title="Clean FastAPI Project")
app.include_router(router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
