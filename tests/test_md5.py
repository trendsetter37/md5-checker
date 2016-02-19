''' Testing MD5 functionality '''
from __future__ import print_function
from md5checker import checkmd5, __init__
import os
import subprocess
import pytest
import json

_DIRECTORY = os.path.dirname(__file__)
_join = os.path.join
DATA_PATH = os.path.abspath(_join(_DIRECTORY, 'data'))
USAGE_PROMPT = 'Usage: md5checker "path-to-file"'

with open(str(_join(DATA_PATH, 'data.json')), 'r') as f:
    files = json.loads(f.read())

FIRST1 = files['file1']['md5']

def test_md5_hash():
    for obj in files.keys():
        filename = _join(DATA_PATH, obj + '.txt')
        assert files[obj]['md5'] == checkmd5.make_hash(filename).upper()

def test_md5_IOError():
    with pytest.raises(IOError):
        checkmd5.make_hash('fake_file.txt')

def test_cli_script():
    res = subprocess.check_output(
        ['md5checker', './tests/data/file1.txt']
    ).strip().decode('utf-8')
    assert res.upper() == FIRST1

def test_cli_with_incorrect_args():
    res = subprocess.check_output(['md5checker']).strip().decode('utf-8')
    assert res == USAGE_PROMPT
