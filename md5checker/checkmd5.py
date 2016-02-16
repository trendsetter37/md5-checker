import sys
import os
from pathlib import Path
import hashlib

def make_file_hash(file_name):
    m = hashlib.md5()
    try:
        path = Path(file_name)
        with path.open(mode='rb') as f:
            contents = f.read()
            m.update(contents)
        return m.hexdigest()
    except IOError as e:
        print('[Errno {}]: {}'.format(e.errno, e.strerror))
        raise e

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print(make_file_hash(file_name))
    else:
        print('Usage: python checkmd5.py path-to-file')
        sys.exit(1)
