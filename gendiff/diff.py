from gendiff.parse_files import parse_files
from gendiff.const import DIFF_CHANGES_TYPES


def diff(file1, file2):
    file_1 = parse_files(file1)
    file_2 = parse_files(file2)
    result_dict = {}

    def make_dict(dict1, dict2, result_dict):
        keys = sorted(set(dict1) | set(dict2))
        for key in keys:
            result_dict[key] = {}
            if key not in dict1:
                result_dict[key] = {
                    'status': DIFF_CHANGES_TYPES.ADDED,
                    'value': dict2[key]
                }
            elif key not in dict2:
                result_dict[key] = {
                    'status': DIFF_CHANGES_TYPES.DELETED,
                    'value': dict1[key]
                }
            elif dict1[key] == dict2[key]:
                result_dict[key] = {
                    'status': DIFF_CHANGES_TYPES.UNCHANGED,
                    'value': dict1[key]
                }
            elif dict1[key] != dict2[key] and (
                not isinstance(dict1[key], dict)
                or not isinstance(dict2[key], dict)
            ):
                result_dict[key] = {
                    'status': DIFF_CHANGES_TYPES.CHANGED,
                    'value_1': dict1[key],
                    'value_2': dict2[key]
                }
            else:
                result_dict[key] = {
                    'status': DIFF_CHANGES_TYPES.NESTED,
                    'value': {}
                }
                _ = make_dict(
                    dict1[key], dict2[key], result_dict[key]['value'])
    make_dict(file_1, file_2, result_dict)
    return result_dict
