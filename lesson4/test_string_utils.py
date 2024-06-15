import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capitalize():
    """Pozitive"""
    assert utils.capitilize("hello") == "Hello"
    assert utils.capitilize("hello girls") == "Hello girls"
    assert utils.capitilize("987") == "987"
    """Negative"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("987hello") == "987hello"


"""trim"""


def test_trim():
    #Pozitive
    assert utils.trim("  Hello") == "Hello"
    assert utils.trim("   hello girls") == "hello girls"
    assert utils.trim(" GIRLS") == "GIRLS"
    #Negative
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_namber_input():
    assert utils.trim(987) == "987"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim("  Hello  ") == "  Hello  "


"""to_list"""


@pytest.mark.parametrize('string, delimeter, result', [
    #Pozitive
    ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3", ",", ["1", "2", "3"]),
    ("$@%@^", "@", ["$", "%", "^"]),
    #Negative
    ("", None, []),
    ("1,2,3", None, ["1", "2", "3"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains"""

@pytest.mark.parametrize('string, symbol, result', [

    ("яблоко", "л", True),
    (" банан", "н", True),
    ("апельсин ", "а", True),
    ("яблоко-банан", "-", True),
    ("", "", True),
    ("123", "2", True),
    ("Банан", "б", False),
    ("яблоко", "а", False),
    ("апельсин", ";", False),
    ("", "2", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


"""delete_symbol"""


@pytest.mark.parametrize('string, symbol, result', [

    ("яблоко", "о", "яблк"),
    ("Стася", "а", "Стся"),
    ("Ветер", "В", "етер"),
    ("987", "8", "97"),
    ("Вкус мандарина", " ", "Вкусмандарина"),

    ("легендарный", "о", "легендарный"),
    ("", "", ""),
    ("", "c", ""),
    ("радость", "", "радость"),
    ("мандарин ", " ", "мандарин"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""starts_with"""


@pytest.mark.parametrize('string, symbol, result', [

    ("кошка", "к", True),
    ("", "", True),
    ("Питер", "П", True),
    ("Way", "W", True),
    ("123", "1", True),

    ("Стася", "с", False),
    ("радость", "Р", False),
    ("", "$", False),
    ("лимонад", "м", False),
    ("123", "2", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_with"""


@pytest.mark.parametrize('string, symbol, result', [

    ("кошка", "а", True),
    ("", "", True),
    ("Питер", "р", True),
    ("Way", "y", True),
    ("123", "3", True),

    ("Стася", "Я", False),
    ("радость", "р", False),
    ("", "$", False),
    ("лимонад", "м", False),
    ("123", "2", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty"""


@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("  ", True),

    ("текст", False),
    ("текст тест", False),
    ("123", False),
    ("%^$", False)
] )
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string"""


@pytest.mark.parametrize('lst, joiner, result', [

    (["Ч", "Г", "У"], ",", "Ч,Г,У"),
    ([9, 8, 7], None, "9, 8, 7"),
    (["кошки", "мышки"], "-", "кошки-мышки"),
    (["Кошки", "мышки"], "ТИРЕ", "КошкиТИРЕмышки"),

    ([], None, ""),
    ([], ",", ""),
    ([], "тире", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result