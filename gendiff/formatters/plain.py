from gendiff.const import DIFF_CHANGES_TYPES


def formatted_data(data):
    match data:
        case False | True:
            return str(data).lower()
        case None:
            return 'null'
        case _:
            if isinstance(data, dict):
                return '[complex value]'
            elif isinstance(data, int):
                return data
            else:
                return f"'{data}'"


def make_plain(diff):
    result = []
    path = []

    def make_key(path):
        return '.'.join(path)

    def make(data, path):
        for key, value in data.items():
            status = value.get('status')
            value_file = value.get('value')
            old_value_file = value.get('old_value')
            new_value_file = value.get('new_value')
            children = value.get('children')
            match status:
                case DIFF_CHANGES_TYPES.ADDED:
                    path.append(key)
                    result.append(f"Property '{make_key(path)}' was added ")
                    result.append(f"with value: {formatted_data(value_file)}\n")
                    path.pop()
                case DIFF_CHANGES_TYPES.DELETED:
                    path.append(key)
                    result.append(f"Property '{make_key(path)}' was removed\n")
                    path.pop()
                case DIFF_CHANGES_TYPES.CHANGED:
                    path.append(key)
                    result.append(f"Property '{make_key(path)}' was updated. ")
                    result.append(f"From {formatted_data(old_value_file)} ")
                    result.append(f"to {formatted_data(new_value_file)}\n")
                    path.pop()
                case DIFF_CHANGES_TYPES.UNCHANGED:
                    continue
                case DIFF_CHANGES_TYPES.NESTED:
                    path.append(key)
                    _ = make(children, path)
                    path.pop()
    make(diff, path)
    return "".join(result)[:-1]
