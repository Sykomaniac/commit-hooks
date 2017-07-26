from __future__ import print_function

import sys
import os
import re
import argparse

from pre_commit_hooks.util import cmd_output

format_regex = re.compile('^([\sA-Za-z0-9\W]+)(\n{2,})([\WA-Za-z0-9]+)|[Mm]erge[.\W]*$')


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filename of commit message')
    args = parser.parse_args(argv)
    retval = 0

    
    for filename in args.filenames:
        with open(filename, 'r') as content:
            commit_msg = content.read()
            if format_regex.search(commit_msg) is None:
                print('Commit message: \n{0}\n Does not match required format'.format(commit_msg))
                retval = 1

    return retval


if __name__ == '__main__':
    sys.exit(main())
