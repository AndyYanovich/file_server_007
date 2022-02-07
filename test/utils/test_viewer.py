import src.utils.viewer as viewer


def test_get_dict_keys_with_2_args ():
    exp_res = 'my folder [folder1] '
    arg1 = 'my folder '
    arg2 = {'folder1' : 'some_folder'}

    act_res = viewer.get_dict_keys(arg1, arg2)
    assert exp_res == act_res


def test_get_dict_keys_with_empty_dict ():
    exp_res = 'my folder'
    arg1 = 'my folder'
    arg2 = {}

    act_res = viewer.get_dict_keys(arg1, arg2)
    assert exp_res == act_res


def test_get_dict_keys_with_empty_string ():
    exp_res = '[folder1] '
    arg1 = ''
    arg2 = {'folder1' : 'some_folder'}

    act_res = viewer.get_dict_keys(arg1, arg2)
    assert exp_res == act_res

