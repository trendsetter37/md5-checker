from __future__ import print_function
from . import checkmd5 as c
import sys
import os
import hashlib
import argparse

make_hash = c.make_hash
_FLAGS = ('-a', '--algo')
__name__ = 'md5checker'
__version__ = '0.2.1'
_ALGOS_26 = (
    'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512'
)

if '2.6' in sys.version:
    hashlib.algorithms_guaranteed = _ALGOS_26


def usage():
    return 'md5checker <file | directory> [options]'


def list_algorithms():
    ''' List available algorithms '''
    return tuple(sorted(list(hashlib.algorithms_guaranteed)))


def optional_flags():
    return 'Optional flags are -a or --algo'

def version():
    return __name__ + ' ' + __version__


parser = argparse.ArgumentParser(
    description='Check hash values for files and directories.',
    usage=usage()
)
parser.add_argument(
    'file', metavar='<file>', nargs='?', help='File to hash.'
)
parser.add_argument(
    '-a', '--algorithm', choices=[a.lower() for a in _ALGOS_26],
    default='md5', metavar='<algorithm>',
    help='Choose hash algorithm to use.'
)
parser.add_argument(
    '-d', '--directory', metavar='<directory>',
    help='Set this if input is a directory.'
)
parser.add_argument(
    '-la', '--list-algorithms', dest='list_algo', action='store_true',
    help='List hash algorithms availble'
)
parser.add_argument(
    '-v', '--version', action='version',
    version=version()
)


def main():
    ''' Entry point for the application script '''
    args = parser.parse_args()
    if args.directory:
        raise NotImplementedError('Not ready for primetime.')
    if args.file:
        print(make_hash(args.file, algo=args.algorithm))
    elif args.list_algo:
        print('\n' + '\n'.join(list_algorithms()))
