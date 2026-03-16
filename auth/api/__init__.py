from api.books import router as books_router
from api.auth import router as auth_router

__all__ = (
    books_router,
    auth_router,
)