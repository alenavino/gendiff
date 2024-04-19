from gendiff.parse_files import parse_files
from gendiff.const import DIFF_CHANGES_TYPES


def make_dict(dict1, dict2, result_dict={}):
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
                'old_value': dict1[key],
                'new_value': dict2[key]
            }
        else:
            result_dict[key] = {
                'status': DIFF_CHANGES_TYPES.NESTED,
                'children': make_dict(dict1[key], dict2[key], result_dict[key])
            }
    return result_dict


def diff(file1, file2):
    data1 = parse_files(file1)
    data2 = parse_files(file2)
    return make_dict(data1, data2)
