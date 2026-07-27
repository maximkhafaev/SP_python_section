from projects_api import ProjectsApi
import pytest
import random

token = ''
api = ProjectsApi('https://ru.yougile.com', token)


@pytest.mark.positive_test
def test_create_project():
    len_before = len(api.get_project_list()['content'])

    title = 'Проект #' + str(random.randint(100, 1000))
    new_project = api.create_project(title)
    id = new_project[0]['id']

    len_after = len(api.get_project_list()['content'])

    get_new = api.get_project_by_id(id)
    title_of_new = get_new[0]['title']

    assert title_of_new == title
    assert len_after - len_before == 1


@pytest.mark.negative_test
def test_create_project_without_token():
    api = ProjectsApi('https://ru.yougile.com', '')
    title = 'Проект #' + str(random.randint(100, 1000))
    new_project = api.create_project(title)

    assert new_project[1] == 401
    assert new_project[0]['message'] == 'Unauthorized'


@pytest.mark.positive_test
def test_get_project_by_id():
    title = 'Проект #' + str(random.randint(100, 1000))
    new_project = api.create_project(title)
    id = new_project[0]['id']

    get_project = api.get_project_by_id(id)

    assert len(get_project[0]) == 3
    assert get_project[0]['id'] == id
    assert get_project[0]['title'] == title


@pytest.mark.negative_test
def test_get_project_by_nonexistent_id():
    get_project = api.get_project_by_id(random.randint(1, 100))

    assert len(get_project[0]) == 3
    assert get_project[1] == 404
    assert get_project[0]['message'] == "Проект не найден"


@pytest.mark.positive_test
def test_change_project():
    title = 'Проект #' + str(random.randint(100, 1000))
    new_project = api.create_project(title)
    id = new_project[0]['id']

    new_title = 'UPD Проект #' + str(random.randint(100, 1000))
    changed_project = api.change_project(id, new_title)

    assert len(changed_project[0]) == 1
    assert changed_project[0]['id'] == id

    changed_project = api.get_project_by_id(id)

    assert changed_project[0]['title'] == new_title


@pytest.mark.negative_test
def test_change_project_to_empty_title():
    title = 'Проект #' + str(random.randint(100, 1000))
    new_project = api.create_project(title)
    id = new_project[0]['id']

    new_title = ''
    changed_project = api.change_project(id, new_title)

    assert changed_project[1] == 400
    assert changed_project[0]['message'][0] == "title should not be empty"
