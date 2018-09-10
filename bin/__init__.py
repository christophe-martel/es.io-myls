# coding: utf-8
"""entry point to run myls module

See readme.md :)
"""
import os
import sys
import logging
import argparse
import myls

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s\t%(asctime)s\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S%z')

def main():
    """Run the app"""
    parser = argparse.ArgumentParser()
    parser.add_argument("baseDirectory", type=str, help="directory to scan")
    parser.add_argument(
        "-u",
        "--unit",
        type=str,
        help="unit",
        choices=myls.HumanReadableByte.available,
        default=myls.HumanReadableByte.defaultUnit
    )

    args = parser.parse_args()
    path = os.path.abspath(args.baseDirectory)

    if not os.path.isdir(path):
        raise Exception(
            'directory "{}" do not exists'.format(args.baseDirectory)
        )

    if not os.access(path, os.R_OK):
        raise Exception(
            'directory "{}" is not readable'.format(args.baseDirectory)
        )

    for file in myls.MyLs(myls.HumanReadableByte(args.unit)).list(path):
        print(file)



if __name__ == '__main__':
    main()
