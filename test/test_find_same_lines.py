from main import find_same_lines

def test_find_same_lines(sample_sets):
    set1, set2 = sample_sets
    same = find_same_lines(set1, set2)
    assert same == set(['line2', 'line3'])