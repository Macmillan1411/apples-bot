from sqlmodel import SQLModel, Field, Column, String
import sqlalchemy.dialects.postgresql as pg
import uuid


class Apple(SQLModel, table=True):
    __tablename__ = "apples"

    # id: int = Field(
    #     sa_column=Column(
    #         Integer,
    #         primary_key=True,
    #         autoincrement=True,
    #         nullable=False,
    #         index=True,

    #     )
    # )

    # uid:uuid.UUID = Field(
    #     sa_column=Column(
    #         pg.UUID,
    #         primary_key=True,
    #         unique=True,
    #         nullable=False
    #     )
    # )
    id: int = Field(default=None, primary_key=True)
    # name: str = Field(
    #     sa_column=Column(
    #         String,
    #         nullable=False,
    #     )
    # )
    name: str
    type: str
    description: str
    image: str

    # def __repr__(self) -> str:
    #     return f"<Apple {self.name}>"
