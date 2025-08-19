import pytest

from find_ft_type import all_thing_is_obj


@pytest.mark.parametrize("ft_list", [
    pytest.param(["Hello", "tata!"], id="str_list"),
    pytest.param([], id="empty_list"),
    pytest.param([1, 2, 3], id="integers_list"),
    pytest.param([1, "hi", None], id="mixed_list"),
    pytest.param([[1, 2], [3, 4]], id="lists_list"),
])
def test_list(capsys, ft_list):
    result = all_thing_is_obj(ft_list)
    captured = capsys.readouterr()
    assert captured.out.strip() == "List : <class 'list'>"
    assert result == 42

    
@pytest.mark.parametrize("ft_tuple", [
    ("Hello", "tata!"),
    (),
    (1, 2, 3),
    (1, "hi", None),
    ([1, 2], [3, 4]),
])
def test_tuple(capsys, ft_tuple):
    result = all_thing_is_obj(ft_tuple)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Tuple : <class 'tuple'>"
    assert result == 42

 
@pytest.mark.parametrize("ft_set", [
    {"Hello", "tata!"},
    {1, 2, 3},
    {1, "hi", None}
])
def test_set(capsys, ft_set):
    result = all_thing_is_obj(ft_set)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Set : <class 'set'>"
    assert result == 42

  
@pytest.mark.parametrize("ft_dict", [
    {"hello": "tata!"},
    {"hello": "tata!", "hi": "toto"},
    {"nb1": 1, "nb2": 2},
    {"arr1": [1,2,3], "arr2": [4,5,6]},
    {},
])
def test_dict(capsys, ft_dict):
    result = all_thing_is_obj(ft_dict)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Dict : <class 'dict'>"
    assert result == 42


@pytest.mark.parametrize("ft_str", [
    "Brian",
    "Toto",
    "Hello",
])
def test_str(capsys, ft_str):
    result = all_thing_is_obj(ft_str)
    captured = capsys.readouterr()
    assert captured.out.strip() == f"{ft_str} is in the kitchen : <class 'str'>"
    assert result == 42


@pytest.mark.parametrize("ft_unknown", [
    42,
    4.2,
    None,
    True,
])
def test_unknown(capsys, ft_unknown):
    result = all_thing_is_obj(ft_unknown)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Type not found"
    assert result == 42


def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}
    all_thing_is_obj(ft_list)
    all_thing_is_obj(ft_tuple)
    all_thing_is_obj(ft_set)
    all_thing_is_obj(ft_dict)
    all_thing_is_obj("Brian")
    all_thing_is_obj("Toto")
    print(all_thing_is_obj(10))

if __name__ == "__main__":
    main()

