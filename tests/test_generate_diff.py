import pytest
from gendiff.generate_diff import generate_diff
from gendiff.const import STYLE_FORMATS


file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file1_yml = 'tests/fixtures/file1.yml'
file2_yml = 'tests/fixtures/file2.yml'
result_stylish = 'tests/fixtures/result_stylish.txt'
result_plain = 'tests/fixtures/result_plain.txt'
result_json = 'tests/fixtures/result_json.txt'


@pytest.mark.parametrize('file1, file2',
                         [(file1_json, file2_json),
                          (file1_yml, file2_yml),
                          (file1_json, file2_yml),
                          (file1_yml, file2_json)])
def test_generate_diff(file1, file2):
    with open(result_stylish) as f:
        assert generate_diff(file1, file2, STYLE_FORMATS.STYLISH) == f.read()
    with open(result_stylish) as f:
        assert generate_diff(file1, file2) == f.read()
    with open(result_plain) as f:
        assert generate_diff(file1, file2, STYLE_FORMATS.PLAIN) == f.read()
    with open(result_json) as f:
        assert generate_diff(file1, file2, STYLE_FORMATS.JSON) == f.read()
