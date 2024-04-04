#!/usr/bin/env python3


import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output')
    args = parser.parse_args()
    diff = generate_diff.generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
