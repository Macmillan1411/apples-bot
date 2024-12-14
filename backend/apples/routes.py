from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


from backend.apples.schemas import AppleSchema, AppleCreateSchema, AppleUpdateSchema
from backend.database import get_session
from backend.apples.apple_service import AppleService


apple_router = APIRouter(prefix="/apples")
apple_service = AppleService()


@apple_router.get("/", response_model=List[AppleSchema])
async def get_all_apples(session: AsyncSession = Depends(get_session)):
    apples = await apple_service.get_all_apples(session)
    print(apples)

    return apples


@apple_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_apple(
    apple_data: AppleCreateSchema, session: AsyncSession = Depends(get_session)
) -> None:
    await apple_service.create_apple(apple_data, session)


@apple_router.get("/{apple_id}", response_model=AppleSchema)
async def get_apple(
    apple_id: int, session: AsyncSession = Depends(get_session)
) -> dict:
    apple = await apple_service.get_apple(apple_id, session)

    if apple:
        return apple.model_dump()
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Apple not found"
        )


@apple_router.patch("/{apple_id}", response_model=AppleSchema)
async def update_apple(
    apple_id: int,
    apple_update_data: AppleUpdateSchema,
    session: AsyncSession = Depends(get_session),
) -> dict:

    updated_apple = await apple_service.update_apple(
        apple_id, apple_update_data, session
    )

    if updated_apple is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Apple not found"
        )
    else:
        return updated_apple


@apple_router.delete("/{apple_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_apple(apple_id: int, session: AsyncSession = Depends(get_session)):
    apple_to_delete = await apple_service.delete_apple(apple_id, session)

    if apple_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Apple not found"
        )
    else:
        return {}
