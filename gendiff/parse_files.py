import json
import yaml
from yaml.loader import SafeLoader


def parse_files(file):
    with open(file) as f:
        if file.endswith('json'):
            data = json.load(f)
        elif file.endswith('yml') or file.endswith('yaml'):
            data = yaml.load(f, Loader=SafeLoader)
        else:
            raise ValueError('Invalid file format!')
    return data
