from gendiff.formatters.stylish import stylish


def format_diff(diff, formatter):
    match formatter:
        case _:
            return stylish(diff)
