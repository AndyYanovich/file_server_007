import pytest
from mock import mock_open

# import src.file_service.file_service
# import src.file_service.file_service as file_service
from src.file_service import file_service
import src.utils.random_values as random_values


@pytest.fixture()
def file_name():
    return 'some_file.txt'


@pytest.fixture()
def file_content():
    return 'Some text\nfrom txt file'


def test_read_file_success(mocker, file_name, file_content):
    exp_res = 'Content :\n' + file_content

    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open)
    mocker.patch("os.path.isfile").return_value = True
    mocked_open().read.return_value = file_content

    act_res = file_service.read_file(file_name)

    mocked_open.assert_called_with(file_name, "r")
    assert exp_res == act_res


def test_read_file_failure(mocker, file_name):
    exp_res = f"File '{file_name}' not exists!!!"

    mocker.patch("os.path.isfile").return_value = False

    with pytest.raises(Exception) as exc:
        file_service.read_file(file_name)
    assert exp_res in str(exc.value)


def test_create_file_success(mocker, file_name, file_content):
    # exp_res = f"File '{file_name}' created"

    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open, create=True)
    mocker.patch("src.utils.random_values.create_rand_string").return_value = file_name
    mocker.patch("os.path.isfile").return_value = False

    file_service.create_file(file_content)
    # act_res = file_service.create_file(file_content)

    mocked_open.assert_called_with(file_name, "w")
    # mocked_open().write.assert_called_with(file_content)
    # assert exp_res == act_res


def test_create_empty_file_success():
    pass


def test_delete_file_success(mocker, file_name):
    exp_res = f"File '{file_name}' deleted"

    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open)
    mocker.patch("os.path.isfile").return_value = True
    mocker.patch("os.remove").return_value = True

    act_res = file_service.delete_file(file_name)

    assert exp_res == act_res


def test_delete_file_failure(mocker, file_name):
    exp_res = f"File '{file_name}' not exists!!!"

    mocked_open = mock_open()
    mocker.patch("builtins.open", mocked_open)
    mocker.patch("os.path.isfile").return_value = False

    with pytest.raises(Exception) as exc:
        file_service.delete_file(file_name)
    assert exp_res in str(exc.value)


def test_list_dir_success():
    pass


def test_change_dir_success():
    pass


def test_change_dir_failure():
    pass


def test_current_dir_success():
    pass


def test_get_file_permissions_success():
    pass


def test_get_file_permissions_no_file_failure():
    pass


def test_set_file_permissions_success():
    pass


def test_set_file_permissions_no_file_failure():
    pass

