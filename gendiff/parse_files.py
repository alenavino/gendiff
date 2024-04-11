import json
import yaml
from yaml.loader import SafeLoader


def parse_files(file):
    with open(file) as f:
        if file.endswith('json'):
            data = json.load(f)
        else:
            data = yaml.load(f, Loader=SafeLoader)
    return data
