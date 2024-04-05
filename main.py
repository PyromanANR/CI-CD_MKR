import os


def find_same_lines(set1, set2):
    same = set()

    for line in set1:
        if line in set2:
            same.add(line)

    return same


def find_diff_lines(set1, set2):
    diff = set()

    for line in set1:
        if line not in set2:
            diff.add(line)

    for line in set2:
        if line not in set1:
            diff.add(line)

    return diff


def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        set1 = set(line.strip() for line in f1)
        set2 = set(line.strip() for line in f2)

    same = find_same_lines(set1, set2)
    diff = find_diff_lines(set1, set2)

    with open(os.path.join('output', 'same.txt'), 'w') as f:
        for line in same:
            f.write(line + '\n')

    with open(os.path.join('output', 'diff.txt'), 'w') as f:
        for line in diff:
            f.write(line + '\n')


if __name__ == '__main__':
    file1 = os.path.join('input', 'file1.txt')
    file2 = os.path.join('input', 'file2.txt')
    compare_files(file1, file2)
