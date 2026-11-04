import allure


@allure.step("Building API client")
def build_api_client():
    with allure.step("Get user authentication tokens"):
        ...
    with allure.step("Create new API client"):
        ...


@allure.step("Creating course, with title '{title}', Step '{step_test}'")
def create_course(title:str, step_test:str):
    ...


@allure.step("Deleting course")
def delete_course():
    ...


def test_feature():
    build_api_client()
    create_course(title="Locust", step_test="one")
    create_course(title="Python", step_test="two")
    create_course(title="Pytest", step_test="three")
    create_course(title="Playtest", step_test="tho")
    delete_course()

# def test_feature():

# with allure.step("Building API client"):
#     ...
#
# with allure.step("Create course"):
#     ...
#
# with allure.step("Deleting course"):
#     assert False
