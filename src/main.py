from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import Settings
from src.routes.users import router as users_router
from src.routes.auth import router as auth_router

app = FastAPI(title="User Management API", version="1.0.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "User Management API"}

if __name__ == "__main__":
    import uvicorn
    settings = Settings()
    uvicorn.run(
        app,
        host=settings.server_host,
        port=settings.server_port,
        log_level=settings.log_level.lower()
    )