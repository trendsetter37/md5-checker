from __future__ import print_function
from . import checkmd5 as c
import sys
import os
import hashlib
make_hash = c.make_hash
_FLAGS = ('-a', '--algo')
__version__ = '0.2.1'
_ALGOS_26 = (
    'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512'
)

if '2.6' in sys.version:
    hashlib.algorithms_guaranteed = _ALGOS_26

def usage():
    response = 'Usage: md5checker "path-to-file" [options]'
    return response


def list_algorithms():
    ''' List available algorithms '''
    return tuple(sorted(list(hashlib.algorithms_guaranteed)))


def optional_flags():
    return 'Optional flags are -a or --algo'


def main(lis=None):
    ''' Entry point for the application script '''
    if lis is not None:
        args = lis
    else:
        args = sys.argv
    length = len(args)

    if length < 2 or length > 4:
        print(usage())
    elif length == 2:
        if args[1] == '-v' or args[1] == '--version':
            print(__version__)
        elif args[1] == '-a' or args[1] == '--algo':
            prompt = 'Available hash algorithms.'
            print(prompt)
            print('-' * len(prompt))
            print('\n'.join(list_algorithms()))
        else:
            print(make_hash(args[1]))
    elif length == 4:
        flag = args[2]
        if flag in _FLAGS:
            print(make_hash(args[1], algo=args[3]))
        else:
            print(optional_flags())
