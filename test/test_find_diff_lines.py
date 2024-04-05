import pytest

from main import find_diff_lines


@pytest.mark.parametrize("set1, set2, expected_diff", [
    (set(['line1', 'line2', 'line3']), set(['line2', 'line3', 'line4']), set(['line1', 'line4'])),
    (set(['line1', 'line2']), set(['line2', 'line3']), set(['line1', 'line3'])),
    (set(['line1', 'line2']), set(['line3', 'line4']), set(['line1', 'line2', 'line3', 'line4'])),
])
def test_find_diff_lines(set1, set2, expected_diff):
    diff = find_diff_lines(set1, set2)
    assert diff == expected_diff
