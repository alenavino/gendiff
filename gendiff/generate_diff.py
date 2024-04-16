from gendiff.diff import diff
from gendiff.const import STYLE_FORMATS
from gendiff.formatters import format_diff


def generate_diff(file1, file2, format_name=STYLE_FORMATS.STYLISH):
    diff_tree = diff(file1, file2)
    return format_diff(diff_tree, format_name)
