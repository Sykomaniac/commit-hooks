from __future__ import print_function

import sys
import os
import re

from pre_commit_hooks.util import cmd_output

format_regex = re.compile('^([\sA-Za-z0-9\W]+)(\n{2,})([\WA-Za-z0-9]+)$')
message_regex = re.compile('(?<=\n\n).*', re.DOTALL)

def get_commit_details(commit):
    return cmd_output(
        'git', 'cat-file', 'commit',
        '{}'.format(commit)
    )

def get_rev_list(new, old):
    return cmd_output(
        'git', 'rev-list',
        '{}..{}'.format(old, new)
    )

def main(argv=None):
    origin = os.environ.get('PRE_COMMIT_ORIGIN')
    source = os.environ.get('PRE_COMMIT_SOURCE')

    if not (origin or source):
        return 1

    revisions = get_rev_list(origin, source).splitlines()
    retval = 0
    
    for commit in revisions:
        details = get_commit_details(commit)
        commit_msg = message_regex.search(details)

        if commit_msg is None:
            retval = 1
            break
        else:
            commit_msg = commit_msg.group(0)

        if format_regex.search(commit_msg) is None:
            print('Commit message: \n{0}\n Does not match required format'.format(commit_msg))
            retval = 1

    return retval


if __name__ == '__main__':
    sys.exit(main())
