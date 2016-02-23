''' Testing MD5 functionality '''
from __future__ import print_function
from md5checker import checkmd5
import os
import subprocess
import shlex
import platform
import pytest
import json

DIRECTORY = os.path.dirname(__file__)
_join = os.path.join
DATA_PATH = os.path.abspath(_join(DIRECTORY, 'data'))
USAGE_PROMPT = 'Usage: md5checker "path-to-file" [options]'
PYTHON_VERSION = platform.python_version()  # Check for python 2.6
SYSTEM = platform.system()
PIPE = subprocess.PIPE

class TestHashes:

    def test_md5_hash(self, files):
        for obj in files.keys():
            filename = _join(DATA_PATH, obj + '.txt')
            assert files[obj]['md5'] == checkmd5.make_hash(filename).upper()

    def test_md5_IOError(self, ):
        with pytest.raises(IOError):
            checkmd5.make_hash('fake_file.txt')

    # Ensure that the package is installed for this to work
    def test_cli_script(self, files):
        args = shlex.split('md5checker ./tests/data/file1.txt')
        if '2.6' not in PYTHON_VERSION:
            res = subprocess.check_output(args).decode('utf-8').strip()
            assert res.upper() == files['file1']['md5']
        else:
            res = make_regression_call_to_cli(args)
            assert res.upper() == files['file1']['md5']

    def test_cli_with_incorrect_args(self):
        args = shlex.split('md5checker')
        if '2.6' not in PYTHON_VERSION:
            res = subprocess.check_output(args).strip().decode('utf-8')
            assert res == USAGE_PROMPT
        else:
            res = make_regression_call_to_cli(args)
            assert res == USAGE_PROMPT

class TestCLI:
    pass

def make_regression_call_to_cli(args):
    ''' return tuple (stdout, stderr) '''
    return subprocess.Popen(args, stdout=PIPE).communicate()[0].strip()

if __name__ == '__main__':
    print(test_cli_script())
