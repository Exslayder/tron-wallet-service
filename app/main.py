import uvicorn
from fastapi import FastAPI
from . import models, database, views
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(views.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
