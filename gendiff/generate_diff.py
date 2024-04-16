from gendiff.diff import diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters import format_diff


def generate_diff(file1, file2, formatter=stylish):
    diff_tree = diff(file1, file2)
    return format_diff(diff_tree, formatter)
