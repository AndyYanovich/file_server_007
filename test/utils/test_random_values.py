import pytest
import src.utils.random_values as random_values


def test_create_rand_string_with_3_symb():
    exp_res = 3
    arg1 = 3

    act_res = len(random_values.create_rand_string(arg1))
    assert exp_res == act_res


def test_create_rand_string_with_a_lot_of_symb():
    exp_res = 30000
    arg1 = 30000

    act_res = len(random_values.create_rand_string(arg1))
    assert exp_res == act_res


def test_create_rand_string_with_0():
    exp_res = 'String should have at least 1 symbol'
    arg1 = 0

    with pytest.raises(Exception) as exc:
        random_values.create_rand_string(arg1)
    assert exp_res in str(exc.value)


def test_create_2_random_string_diff():
    res1 = random_values.create_rand_string(100)
    res2 = random_values.create_rand_string(100)
    assert res1 != res2
