''' Testing MD5 functionality '''
from __future__ import print_function
from md5checker import checkmd5
import os
import subprocess
import shlex
import platform
import pytest
import json

_DIRECTORY = os.path.dirname(__file__)
_join = os.path.join
DATA_PATH = os.path.abspath(_join(_DIRECTORY, 'data'))
USAGE_PROMPT = 'Usage: md5checker "path-to-file"'
PYTHON_VERSION = platform.python_version()  # Check for python 2.6
SYSTEM = platform.system()


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
    if '2.6' not in PYTHON_VERSION:
        res = subprocess.check_output(
            ['md5checker', './tests/data/file1.txt']
        ).decode('utf-8').strip()
        assert res.upper() == FIRST1
    else:
        args = shlex.split('md5checker ./tests/data/fil1.txt')
        res = subprocess.Popen(args).decode('utf-8').strip()
        assert res == FIRST1

def test_cli_with_incorrect_args():
    res = subprocess.check_output(['md5checker']).strip().decode('utf-8')
    assert res == USAGE_PROMPT

if __name__ == '__main__':
    print(test_cli_script())
