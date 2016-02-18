''' Testing MD5 functionality '''
from __future__ import print_function
from md5checker import checkmd5
import os
import json

_DIRECTORY = os.path.dirname(__file__)
_join = os.path.join
DATA_PATH = os.path.abspath(_join(_DIRECTORY, 'data'))

with open(str(_join(DATA_PATH, 'data.json')), 'r') as f:
    files = json.loads(f.read())

def test_md5_hash():
    for obj in files.keys():
        filename = _join(DATA_PATH, obj + '.txt')
        assert files[obj]['md5'] == checkmd5.make_hash(filename).upper()
