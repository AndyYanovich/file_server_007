import pytest
import os


# patch
# m = mock.patch('os.path.exists')


@pytest.fixture()
def my_fixture3():
    return 3


@pytest.fixture()
def my_fixture4():
    return 3


def test_example(my_fixture3, my_fixture4):
    assert my_fixture3 == my_fixture4


def test_example2():
    assert 4 == 4


def test_with_mock(mocker):
    m = mocker.patch('os.path.exists')
    m.return_value = []
    res = os.path.exists('main.py')
    assert res == []


#


def sum(a, b):
    return a + b


def test_sum1(mocker):
    mocker.patch(__name__ + ".sum", return_value=9)
    assert sum(2, 3) == 9


def test_sum2(mocker):
    def crazy_sum(a, b):
        return b + b

    mocker.patch(__name__ + ".sum", side_effect=crazy_sum)
    assert sum(2, 3) == 6
