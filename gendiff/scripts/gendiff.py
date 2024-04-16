#!/usr/bin/env python3


from gendiff.cli import parser_args
from gendiff import generate_diff


def main():
    args = parser_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        args.format)
    print(diff)


if __name__ == '__main__':
    main()
