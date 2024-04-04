import json


def generate_diff(file1, file2):
    with (
        open(file1) as f1,
        open(file2) as f2
    ):
        file_1 = json.load(f1)
        file_2 = json.load(f2)
        result = ['{\n']
        keys = sorted(set(file_1) | set(file_2))
        for key in keys:
            if key in file_1 and key in file_2:
                if file_1[key] == file_2[key]:
                    result.append(
                        f'    {key}: {str(file_1[key]).lower()}\n')
                else:
                    result.extend(
                        [f'  - {key}: {str(file_1[key]).lower()}\n',
                            f'  + {key}: {str(file_2[key]).lower()}\n'])
            elif key in file_1:
                result.append(f'  - {key}: {str(file_1[key]).lower()}\n')
            elif key in file_2:
                result.append(f'  + {key}: {str(file_2[key]).lower()}\n')
        result.append('}')
        return ''.join(result)
