from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, calls
from app.middleware.error_handler import ErrorHandlerMiddleware


app = FastAPI(title="Logistics Voice Agent Backend", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ErrorHandlerMiddleware)

# register routers
app.include_router(auth.router)
app.include_router(calls.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
