from main import find_diff_lines


def test_find_diff_lines(sample_sets):
    set1, set2 = sample_sets
    diff = find_diff_lines(set1, set2)
    assert diff == set(['line1', 'line4'])
