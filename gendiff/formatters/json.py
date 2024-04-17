from gendiff.const import DIFF_CHANGES_TYPES


def formatted_data(data):
    match data:
        case False:
            return str(data).lower()
        case True:
            return str(data).lower()
        case None:
            return 'null'
        case _:
            if isinstance(data, int):
                return data
            return f'"{data}"'


def make_tree(data, depth, indent='  '):
    result = []

    def make(data, depth):
        if not isinstance(data, dict):
            result.append(f'{formatted_data(data)}')
        else:
            result.append('{')
            for key, value in data.items():
                depth += 1
                result.append(f'\n{indent * depth}{formatted_data(key)}: ')
                _ = make(value, depth)
                depth -= 1
                result.append(',')
            result.pop()
            result.append(f'\n{indent * depth}}}')
    make(data, depth)
    return result


def make_unchanged_tree(key, value, status, indent, depth, result):
    result.append(f'\n{indent * depth}{formatted_data(key)}: {{')
    depth += 1
    result.append(f'\n{indent * depth}"status": "{status}",')
    result.append(f'\n{indent * depth}"value": ')
    result.extend(make_tree(value, depth))
    depth -= 1
    result.append(f'\n{indent * depth}}}')
    return result


def make_changed_tree(key, old_value, new_value, status, indent, depth, result):
    result.append(f'\n{indent * depth}{formatted_data(key)}: {{')
    depth += 1
    result.append(f'\n{indent * depth}"status": "{status}",')
    result.append(f'\n{indent * depth}"old_value": ')
    result.extend(make_tree(old_value, depth))
    result.append(',')
    result.append(f'\n{indent * depth}"new_value": ')
    result.extend(make_tree(new_value, depth))
    depth -= 1
    result.append(f'\n{indent * depth}}}')
    return result


def make_json(diff):
    result = ['{']
    depth = 1
    indent = '  '

    def make_result(data, depth):
        for key, value in data.items():
            status = value.get('status')
            value_file = value.get('value')
            old_value_file = value.get('old_value')
            new_value_file = value.get('new_value')
            children = value.get('children')
            match status:
                case DIFF_CHANGES_TYPES.ADDED:
                    _ = make_unchanged_tree(key, value_file, status,
                                            indent, depth, result)
                case DIFF_CHANGES_TYPES.DELETED:
                    _ = make_unchanged_tree(key, value_file, status,
                                            indent, depth, result)
                case DIFF_CHANGES_TYPES.UNCHANGED:
                    _ = make_unchanged_tree(key, value_file, status,
                                            indent, depth, result)
                case DIFF_CHANGES_TYPES.CHANGED:
                    _ = make_changed_tree(key, old_value_file, new_value_file,
                                          status, indent, depth, result)
                case _:
                    result.append(f'\n{indent * depth}')
                    result.append(f'{formatted_data(key)}: {{')
                    depth += 1
                    result.append(f'\n{indent * depth}"status": "{status}",')
                    result.append(f'\n{indent * depth}"children": {{')
                    depth += 1
                    _ = make_result(children, depth)
                    depth -= 1
                    result.append(f'\n{indent * depth}}}')
                    depth -= 1
                    result.append(f'\n{indent * depth}}}')
            result.append(',')
        result.pop()
        return result
    make_result(diff, depth)
    depth -= 1
    result.append(f'\n{indent * depth}}}')
    return ''.join(result)
