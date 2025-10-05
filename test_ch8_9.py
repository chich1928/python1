import pytest
from ch8_9 import is_valid_string, clean_string, process


def test_is_valid_string():
    assert is_valid_string("hello") is True
    assert is_valid_string("   hi ") is True
    assert is_valid_string("") is False
    assert is_valid_string("   ") is False
    assert is_valid_string(None) is False
    assert is_valid_string(123) is False


def test_clean_string():
    assert clean_string(" Hello ") == "hello"
    assert clean_string("WoRLd") == "world"


def test_process():
    data = [" Hello ", "", None, "  ", "WoRLd  ", 123]
    assert process(data) == ["hello", "world"]
