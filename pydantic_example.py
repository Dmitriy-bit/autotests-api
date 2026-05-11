from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")  # алиас для поля


user_data = {
    'id': 1,
    'name': 'Alice',
    'email': 'alice@example.com',
    'isActive': True

}
user = User(**user_data)  # распаковка словаря user_data
print(user.model_dump())  # преобразование в словарь
print(user.model_dump_json())  # преобразование в строку json
