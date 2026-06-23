from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.users.users_schema import UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет что ответ на создание пользователя соответствует запросу.

    :param request: Исходный зарос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет что ответ, на запрос получения данных пользователя соответствует ответу, на запрос создания пользователя.

    :param actual: Данные пользователя полученные в запросе на получение данных о пользователе.
    :param expected: Данные пользователя полученные при создании пользователя.
    :raises AssertionError: Если полученные данные о пользователе не совпадают с данными полученными при его создании.
    """
    assert_equal(actual.id, expected.id, "user_id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")


def assert_get_user_response(get_user_response: UserSchema, create_user_response: UserSchema):
    """
    Проверяет, что данные пользователя совпадают с данными полученными при его создании:

    :param get_user_response: Данные в ответе на запрос получения данных пользователя.
    :param create_user_response: Данные в ответе на запрос создания пользователя.
    :return:
    """
    assert_user(get_user_response, create_user_response)
