import os

from main import compare_files


def test_compare_files(sample_files):
    file1, file2 = sample_files
    compare_files(file1, file2)

    with open(os.path.join('output', 'same.txt'), 'r') as f:
        same = f.read()
    assert 'line2' in same
    assert 'line3' in same

    with open(os.path.join('output', 'diff.txt'), 'r') as f:
        diff = f.read()
    assert 'line1' in diff
    assert 'line4' in diff
