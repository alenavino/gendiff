from gendiff.parse_files import parse_files


def diff(file1, file2):
    file_1 = parse_files(file1)
    file_2 = parse_files(file2)
    result_dict = {}

    def make_dict(dict1, dict2, result_dict):
        keys = sorted(set(dict1) | set(dict2))
        for key in keys:
            result_dict[key] = {}
            if key not in dict1:
                result_dict[key]['status'] = 'added'
                result_dict[key]['value'] = dict2[key]
            elif key not in dict2:
                result_dict[key]['status'] = 'deleted'
                result_dict[key]['value'] = dict1[key]
            elif dict1[key] == dict2[key]:
                result_dict[key]['status'] = 'unchanged'
                result_dict[key]['value'] = dict1[key]
            elif dict1[key] != dict2[key] and (
                not isinstance(dict1[key], dict)
                or not isinstance(dict2[key], dict)
            ):
                result_dict[key]['status'] = 'changed'
                result_dict[key]['value_1'] = dict1[key]
                result_dict[key]['value_2'] = dict2[key]
            else:
                result_dict[key]['status'] = 'changed inside'
                result_dict[key]['value'] = {}
                _ = make_dict(
                    dict1[key], dict2[key], result_dict[key]['value'])
    make_dict(file_1, file_2, result_dict)
    return result_dict
