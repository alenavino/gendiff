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
            if isinstance(data, dict):
                return '[complex value]'
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
            value_1file = value.get('value_1')
            value_2file = value.get('value_2')
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
                    result.append(f"From {formatted_data(value_1file)} ")
                    result.append(f"to {formatted_data(value_2file)}\n")
                    path.pop()
                case DIFF_CHANGES_TYPES.UNCHANGED:
                    continue
                case DIFF_CHANGES_TYPES.NESTED:
                    path.append(key)
                    _ = make(value_file, path)
                    path.pop()
    make(diff, path)
    return "".join(result)[:-1]
