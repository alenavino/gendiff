from gendiff.const import STYLE_FORMATS
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain


def format_diff(diff, format_name):
    match format_name:
        case STYLE_FORMATS.STYLISH:
            return make_stylish(diff)
        case STYLE_FORMATS.PLAIN:
            return make_plain(diff)
