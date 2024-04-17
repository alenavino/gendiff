import pytest
from gendiff.generate_diff import generate_diff
from gendiff.const import STYLE_FORMATS


file1 = 'tests/fixtures/file1.json'
file2 = 'tests/fixtures/file2.json'
result_stylish = 'tests/fixtures/result_stylish.txt'
file3 = 'tests/fixtures/file1.yml'
file4 = 'tests/fixtures/file2.yml'
file5 = 'tests/fixtures/file1_nested.yml'
file6 = 'tests/fixtures/file2_nested.yml'
result_nested_stylish = 'tests/fixtures/result_nested_stylish.txt'
result_nested_plain = 'tests/fixtures/result_nested_plain.txt'
result_nested_json = 'tests/fixtures/result_nested_json.txt'


@pytest.mark.parametrize('file1, file2, expected, format_name',
                         [(file1, file2, result_stylish, STYLE_FORMATS.STYLISH),
                          (file3, file4, result_stylish, STYLE_FORMATS.STYLISH),
                          (file5, file6, result_nested_stylish,
                           STYLE_FORMATS.STYLISH),
                          (file5, file6, result_nested_plain,
                           STYLE_FORMATS.PLAIN),
                          (file5, file6, result_nested_json,
                           STYLE_FORMATS.JSON)])
def test_generate_diff(file1, file2, expected, format_name):
    with open(expected) as f:
        assert generate_diff(file1, file2, format_name) == f.read()
