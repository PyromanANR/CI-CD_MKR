import pytest

@pytest.fixture
def sample_files(tmpdir):
    content1 = 'line1\nline2\nline3\n'
    content2 = 'line2\nline3\nline4\n'
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")
    file1.write(content1)
    file2.write(content2)
    return str(file1), str(file2)