import pytest

from NULL_not_found import NULL_not_found


def test_none(capsys):
    result = NULL_not_found(None)
    captured = capsys.readouterr().out.strip()
    assert captured == "Nothing: None <class 'NoneType'>"
    assert result == 0


def test_float(capsys):
    result = NULL_not_found(float("NaN"))
    captured = capsys.readouterr().out.strip()
    assert captured == "Cheese: nan <class 'float'>"
    assert result == 0


def test_zero(capsys):
    result = NULL_not_found(0)
    captured = capsys.readouterr().out.strip()
    assert captured == "Zero: 0 <class 'int'>"
    assert result == 0


def test_empty(capsys):
    result = NULL_not_found("")
    captured = capsys.readouterr().out.strip()
    assert captured == "Empty:  <class 'str'>"
    assert result == 0


def test_false(capsys):
    result = NULL_not_found(False)
    captured = capsys.readouterr().out.strip()
    assert captured == "Fake: False <class 'bool'>"
    assert result == 0

@pytest.mark.parametrize("mixed", [
    pytest.param(["Hello", "tata!"], id="list"),
    pytest.param([], id="empty list"),
    pytest.param(("Hello", "tata!"), id="tuple"),
    pytest.param((), id="empty tuple"),
    pytest.param({"Hello": "tata!"}, id="dictionary"),
    pytest.param({}, id="empty dictionary"),
    pytest.param(42, id="integer"),
    pytest.param(4.2, id="float"),
    pytest.param(True, id="bool"),
])
def test_not_found(capsys, mixed):
    result = NULL_not_found(mixed)
    captured = capsys.readouterr().out.strip()
    assert captured == "Type not Found"
    result == 1


  
def main():
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))



if __name__ == "__main__":
    main()
    