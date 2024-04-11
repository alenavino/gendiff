import pytest
from gendiff.generate_diff import generate_diff


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'
result = 'tests/fixtures/result.txt'
file3 = 'tests/fixtures/file3.yml'
file4 = 'tests/fixtures/file4.yml'


@pytest.mark.parametrize('file1, file2, expected', [(file1, file2, result),
                                                    (file3, file4, result)])
def test_generate_diff(file1, file2, expected):
    with open(expected) as f:
        assert generate_diff(file1, file2) == f.read()
