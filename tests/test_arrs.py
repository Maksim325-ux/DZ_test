from utils import arrs
import pytest

@pytest.fixture
def list_test():
    return [1, 2, 3]


def test_get(list_test):
    assert arrs.get(list_test, 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice(list_test):
    assert arrs.my_slice(list_test, 1, 3) == [2, 3]
    assert arrs.my_slice(list_test, 1) == [2, 3]
    assert arrs.my_slice(list_test, 0, -1) == [1, 2]
    assert arrs.my_slice([], 0, -1) == []
    assert arrs.my_slice(list_test, -1, -3) == []
    assert arrs.my_slice(list_test, -4) == [1, 2, 3]
