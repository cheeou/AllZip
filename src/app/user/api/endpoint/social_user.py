from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from src.app.user.api.dependencies import google_oauth_service
from src.app.user.model.user import User
from src.app.user.schema.social_user import UserResponse
from fastapi import Response

router = APIRouter()


@router.post("/google", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def register_google_user(
        user: Annotated[User, Depends(google_oauth_service.register_social_user)],
) -> UserResponse:
    # Convert the SQLAlchemy User model to a Pydantic model and return
    return UserResponse.from_orm(user)
