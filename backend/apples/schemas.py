from pydantic import BaseModel


class AppleSchema(BaseModel):
    id: int
    name: str
    type: str
    description: str
    image: str

    class Config:
        from_attributes = True


class AppleUpdateSchema(BaseModel):
    name: str
    type: str
    description: str
    image: str

    class Config:
        from_attributes = True


class AppleCreateSchema(BaseModel):
    """
    This class is used to validate the request when creating or updating an apple
    """

    name: str
    type: str
    description: str
    image: str
