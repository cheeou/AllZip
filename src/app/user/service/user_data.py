from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from webtool.auth import AuthData

from src.app.user.repository.user_data import UserDataRepository
from src.app.user.schema.user_data import PartialUserDataDto, UserDataDto
from src.core.dependencies.db import postgres_session
from src.core.dependencies.oauth import get_current_user


class UserDataService:
    def __init__(self, repository: UserDataRepository):
        self.repository = repository

    async def create_user_data(
        self,
        data: UserDataDto,
        session: postgres_session,
        auth_data: AuthData = Depends(get_current_user),
    ):
        try:
            await self.repository.create(
                session,
                sub=auth_data.identifier,
                **data.model_dump(exclude_unset=True),
            )
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    async def read_user_data(
        self,
        session: postgres_session,
        auth_data: AuthData = Depends(get_current_user),
    ):
        result = await self.repository.get(
            session,
            [self.repository.model.sub == auth_data.identifier],
        )

        return result.mappings().first()

    async def update_user_data(
        self,
        data: PartialUserDataDto,
        session: postgres_session,
        auth_data: AuthData = Depends(get_current_user),
    ):
        await self.repository.update(
            session,
            [self.repository.model.sub == auth_data.identifier],
            **data.model_dump(exclude_unset=True),
        )
