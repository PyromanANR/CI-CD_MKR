import pytest
from main import find_same_lines

@pytest.mark.parametrize("set1, set2, expected_same", [
    (set(['line1', 'line2', 'line3']), set(['line2', 'line3', 'line4']), set(['line2', 'line3'])),
    (set(['line1', 'line2']), set(['line2', 'line3']), set(['line2'])),
    (set(['line1', 'line2']), set(['line3', 'line4']), set([])),
])
def test_find_same_lines(set1, set2, expected_same):
    same = find_same_lines(set1, set2)
    assert same == expected_same