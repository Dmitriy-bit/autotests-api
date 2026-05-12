from pydantic import BaseModel, Field, ConfigDict, EmailStr, constr
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Структура Pydantic модели данных пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel,
                              populate_by_name=True
                              )
    id: str
    email: EmailStr
    last_name: constr(min_length=2) = Field(alias="lastName")
    first_name: constr(min_length=2) = Field(alias="firstName")
    middle_name: constr(min_length=2) = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Структура Pydantic модели запроса на создание пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel,
                              populate_by_name=True
                              )
    email: EmailStr = Field(default="user@example.com")
    password: constr(min_length=6)
    last_name: constr(min_length=2)
    first_name: constr(min_length=2)
    middle_name: constr(min_length=2)


class CreateUserResponseSchema(BaseModel):
    """
    Структура Pydantic модели ответа с данными созданного пользователя
    """
    user: UserSchema
