def formatted_data(data):
    match data:
        case False:
            return str(data).lower()
        case True:
            return str(data).lower()
        case None:
            return 'null'
        case _:
            return str(data)


def make_tree(data, depth, indent='    '):
    result = []

    def make(data, depth):
        if not isinstance(data, dict):
            result.append(f'{formatted_data(data)}\n')
        else:
            result.append('{\n')
            for key, value in data.items():
                depth += 1
                result.append(f'{indent * depth}{indent}{key}: ')
                _ = make(value, depth)
                depth -= 1
            result.append(f'{indent * depth}{indent}}}\n')
    make(data, depth)
    return result


def stylish(tree):
    result = ['{\n']
    depth = 0
    indent = '    '
    indent_add = '  + '
    indent_del = '  - '

    def make_result(data, depth):
        for key, value in data.items():
            status = value.get('status')
            value_file = value.get('value')
            value_1file = value.get('value_1')
            value_2file = value.get('value_2')
            match status:
                case 'added':
                    result.append(f'{indent * depth}{indent_add}{key}: ')
                    result.extend(make_tree(value_file, depth))
                case 'deleted':
                    result.append(f'{indent * depth}{indent_del}{key}: ')
                    result.extend(make_tree(value_file, depth))
                case 'unchanged':
                    result.append(f'{indent * depth}{indent}{key}: ')
                    result.extend(make_tree(value_file, depth))
                case 'changed':
                    result.append(f'{indent * depth}{indent_del}{key}: ')
                    result.extend(make_tree(value_1file, depth))
                    result.append(f'{indent * depth}{indent_add}{key}: ')
                    result.extend(make_tree(value_2file, depth))
                case _:
                    result.append(f'{indent * depth}{indent}{key}: {{\n')
                    depth += 1
                    _ = make_result(value_file, depth)
                    depth -= 1
                    result.append(f'{indent * depth}{indent}}}\n')
        return result
    make_result(tree, depth)
    result.append(f'{indent * depth}}}\n')
    return ''.join(result)
