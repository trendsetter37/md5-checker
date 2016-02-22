from __future__ import print_function
from . import checkmd5 as c
import sys
import os
make_hash = c.make_hash
_FLAGS = ('-a', '--algo')

def main():
    ''' Entry point for the application script '''
    args = sys.argv
    length = len(args)

    if length < 2 or 4 < length <= 3:
        print('Usage: md5checker "path-to-file" [options]')
    elif length == 2:
        print(make_hash(args[1]))
    elif length == 4:
        flag = args[2]
        if flag in _FLAGS:
            print(make_hash(args[1], algo=args[3]))
        else:
            print('Optional flags are -a or --algo')
            sys.exit(1)
