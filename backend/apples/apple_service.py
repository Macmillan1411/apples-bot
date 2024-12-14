from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from backend.apples.models import Apple
from backend.apples.schemas import AppleUpdateSchema, AppleCreateSchema


class AppleService:
    """
    This class provides methods to create, read, update, and delete apples
    """

    async def get_all_apples(self, session: AsyncSession):
        """
        Get a list of all apples

        Returns:
            list: list of apples
        """
        statement = select(Apple)
        result = await session.execute(statement)
        return result.scalars().all()

    async def create_apple(self, apple_data: AppleCreateSchema, session: AsyncSession):
        """
        Create a new apple

        Args:
            apple_data (AppleCreateSchema): data to create a new apple

        Returns:
            Apple: the new apple
        """

        apple_data_dict = apple_data.model_dump()
        new_apple = Apple(**apple_data_dict)

        session.add(new_apple)
        await session.commit()
        await session.refresh(new_apple)

    async def get_apple(self, apple_id: int, session: AsyncSession):
        """Get an apple by its ID.

        Args:
            apple_id (int): the ID of the apple

        Returns:
            Apple: the apple object
        """
        statement = select(Apple).where(Apple.id == apple_id)

        result = await session.execute(statement)
        apple = result.scalar_one_or_none()

        return apple if apple is not None else None

    async def update_apple(
        self, apple_id: str, update_data: AppleUpdateSchema, session: AsyncSession
    ):
        """Update a apple

        Args:
            apple_id (int): the ID of the apple
            update_data (AppleCreateSchema): the data to update the apple

        Returns:
            Apple: the updated apple
        """

        apple_to_update = await self.get_apple(apple_id, session)

        if apple_to_update is not None:
            update_data_dict = update_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(apple_to_update, k, v)

            await session.commit()

            return apple_to_update.model_dump()
        else:
            return None

    async def delete_apple(self, apple_id: str, session: AsyncSession):
        """Delete a apple
        Args:
            apple_id (int): the ID of the apple
        """
        apple_to_delete = await self.get_apple(apple_id, session)

        if apple_to_delete is not None:
            await session.delete(apple_to_delete)

            await session.commit()

            return {}

        else:
            return None
