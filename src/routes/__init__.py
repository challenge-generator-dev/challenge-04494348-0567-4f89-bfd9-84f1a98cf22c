from fastapi import APIRouter
from src.routes.users import router as users_router
from src.routes.auth import router as auth_router

api_router = APIRouter()

api_router.include_router(
    users_router,
    prefix="/users",
    tags=["users"]
)

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)

__all__ = ["api_router", "users_router", "auth_router"]