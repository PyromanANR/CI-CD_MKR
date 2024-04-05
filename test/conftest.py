import pytest

@pytest.fixture
def sample_sets():
    set1 = set(['line1', 'line2', 'line3'])
    set2 = set(['line2', 'line3', 'line4'])
    return set1, set2