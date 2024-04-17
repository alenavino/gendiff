from gendiff.const import STYLE_FORMATS
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def format_diff(diff, format_name):
    match format_name:
        case STYLE_FORMATS.JSON:
            return make_json(diff)
        case STYLE_FORMATS.PLAIN:
            return make_plain(diff)
        case _:
            return make_stylish(diff)
