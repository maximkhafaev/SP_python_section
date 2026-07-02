from string_utils import StringUtils
import pytest

utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('string, result', [('hello', 'Hello')])
def test_capitalize_positive(string, result):
    assert utils.capitalize(string) == result


@pytest.mark.negative
@pytest.mark.parametrize('string, result', [
    ('Hello', 'Hello'),
    ('123', '123'),
    ('', ''),
    ('   hello', '   hello')
])
def test_capitalize_negative(string, result):
    assert utils.capitalize(string) == result


@pytest.mark.positive
@pytest.mark.parametrize('string, result', [
    (' hello', 'hello'),
    ('   hello', 'hello'),
    (' hi ', 'hi ')
])
def test_trim_positive(string, result):
    assert utils.trim(string) == result


@pytest.mark.negative
@pytest.mark.parametrize('string, result', [
    ('hi ', 'hi '),
    ('', ''),
    ('   ', '')
])
def test_trim_negative(string, result):
    assert utils.trim(string) == result


@pytest.mark.positive
@pytest.mark.parametrize('string, look_for, result', [
    ('hello', 'el', True),
    ('Hello ', ' ', True),
    ('12 января', '12', True)
])
def test_contains_positive(string, look_for, result):
    assert utils.contains(string, look_for) == result


@pytest.mark.negative
@pytest.mark.parametrize('string, look_for, result', [
    ('', 'l', False),
    ('Thomas', 'b', False),
    ('great', 'G', False),
    ('bb', 'bbbb', False),
    ('aбв', 'а', False)  # в исходной строке а - английская, ищем русскую а
])
def test_contains_negative(string, look_for, result):
    assert utils.contains(string, look_for) == result


@pytest.mark.positive
@pytest.mark.parametrize('string, deleting, result', [
    (' hello ', ' ', 'hello'),
    ('   ', ' ', ''),
    ('brave', 'ave', 'br'),
    ('man', 'man', '')
])
def test_delete_positive(string, deleting, result):
    assert utils.delete_symbol(string, deleting) == result


@pytest.mark.positive
@pytest.mark.parametrize('string, deleting, result', [
    ('looking', 'book', 'looking'),
    ('aaa', 'aaaa', 'aaa'),
    ('', '', ''),
    ('aбв', 'а', 'aбв')  # в исходной строке а - анлийская, удаляем русскую а
])
def test_delete_negative(string, deleting, result):
    assert utils.delete_symbol(string, deleting) == result


def test_delete_none_negative():
    with pytest.raises(TypeError):
        utils.delete_symbol('Test', None)
