import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),  # обычное слово
        ("python", "Python"),  # строка с маленькими буквами
        ("skypro academy", "Skypro academy"),  # строка с несколькими словами
    ],
)
def test_capitalize_positive(string_utils, input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected_exception",
    [
        ("135ace", None),  # цифры с буквами в строке
        ("", None),  # пустая строка
        ("   ", None),  # строка с пробелами
        (None, AttributeError),  # None значение
    ],
)
def test_capitalize_negative(string_utils, input_str, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            string_utils.capitalize(input_str)
    else:
        assert string_utils.capitalize(input_str) == input_str


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   leadership", "leadership"),  # удаление пробелов в начале строки
        ("   brave heart", "brave heart",),
        # удаление пробелов только в начале строки
        ("importance", "importance"),  # строка без пробелов в начале
    ],
)
def test_trim_positive(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),  # пустая строка, результат - пустая строка
        ("   ", ""),  # строка только с пробелами, результат - пустая строка
        ("text", "text"),  # строка без пробелов, результат - такая же строка
    ],
)
def test_trim_negative(string_utils, input_str, expected):
    assert string_utils.trim(input_str) == expected


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("leadership", "l", True),  # символ найден в строке
        ("leadership", "d", True),  # символ найден в строке
        ("leadership", "w", False),  # символ не найден в строке
    ],
)
def test_contains_positive(string_utils, input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("", " ", False),  # пустая строка и пробел, результат False
        ("leadership", "L", False),
        # непустая строка и заглавная буква, результат False
        ("leadership", "z", False),
        # символ не найден в строке, результат False
    ],
)
def test_contains_negative(string_utils, input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# Позитивные тесты
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("leadership", "l", "eadership"),  # удаление одиночного символа
        ("hello world", "o", "hell wrld"),  # удаление всех вхождений символа
        ("aceaceace", "ace", ""),  # удаление всей подстроки
    ],
)
def test_delete_symbol_positive(string_utils, input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


# Негативные тесты
@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("leadership", "", "leadership"),
        # удаление пустого символа, строка не изменяется
        ("leadership", "w", "leadership"),
        # символ отсутствует, строка не изменяется
        ("", "b", ""),
        # удаление символа из пустой строки, результат пустая строка
    ],
)
def test_delete_symbol_negative(string_utils, input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
