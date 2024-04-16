from collections import namedtuple

_STYLE_FORMAT_VALUES = ('stylish', 'plain', 'json')
STYLE_FORMATS = (namedtuple('FormatChoices',
                            map(str.upper, _STYLE_FORMAT_VALUES))(*_STYLE_FORMAT_VALUES))  # noqa

_DIFF_CHANGES_TYPE = ('deleted', 'added', 'nested', 'changed', 'unchanged')
DIFF_CHANGES_TYPES = (namedtuple('FormatTypes',
                                 map(str.upper, _DIFF_CHANGES_TYPE))(*_DIFF_CHANGES_TYPE))  # noqa

# _DATA_FORMATS_VALUE = ('json', 'yaml', 'yml')
# DATA_FORMATS = (namedtuple('DataFormats',
#                            map(str.upper, _DATA_FORMATS_VALUE))(*_DATA_FORMATS_VALUE))  # noqa
