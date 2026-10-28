import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ---------- capitalize ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", " "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_keeps_rest_of_string():
    # Дефект: остальные буквы не должны менять регистр
    assert string_utils.capitalize("SkyPro") == "SkyPro"


@pytest.mark.negative
def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# ---------- trim ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("  04 апреля 2023", "04 апреля 2023"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("skypro   ", "skypro   "),  # пробелы в конце не удаляются
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# ---------- contains ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("123", "1", True),
    ("04 апреля 2023", " ", True),
    ("SkyPro", "Pro", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "s", False),  # регистр важен
    ("", "a", False),
    (" ", "a", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")


# ---------- delete_symbol ----------
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("04 апреля 2023", "0", "4 апреля 223"),
    ("hello world", "o", "hell wrld"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("leadership", "w", "leadership"),
    ("", "b", ""),
    (" ", "0", " "),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
