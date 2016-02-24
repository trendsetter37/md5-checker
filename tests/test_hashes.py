''' Testing MD5 functionality '''
from __future__ import print_function
import md5checker
import os
import subprocess
import shlex
import platform
import pytest
import json

checkmd5 = md5checker.checkmd5
VERSION = md5checker.__version__
DIRECTORY = os.path.dirname(__file__)
_join = os.path.join
DATA_PATH = os.path.abspath(_join(DIRECTORY, 'data'))
USAGE_PROMPT = 'Usage: md5checker "path-to-file" [options]'
ALGOS = """Available hash types
--------------------

md5
sha1
sha224
sha256
sha384
sha512"""
OPTIONAL_FLAGS = 'Optional flags are -a or --algo'
PYTHON_VERSION = platform.python_version()  # Check for python 2.6
SYSTEM = platform.system()
PIPE = subprocess.PIPE
FILES = json.loads(open('tests/data/data.json', 'r').read())

def create_parameters(algo):
    return [(FILES[x]['input_file'], FILES[x][algo]) for x in FILES.keys()]

@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('md5')
)
def test_md5_hash(input_file, output):
    assert checkmd5.make_hash(locate_data(input_file)) == output

@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha1')
)
def test_sha1_hash(input_file, output):
    assert checkmd5.make_hash(locate_data(input_file), algo='sha1') == output

@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha224')
)
def test_sha224_hash(input_file, output):
    assert checkmd5.make_hash(locate_data(input_file), algo='sha224') == output

@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha256')
)
def test_sha256_hash(input_file, output):
    assert checkmd5.make_hash(locate_data(input_file), algo='sha256') == output

@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha384')
)
def test_sha384_hash(input_file, output):
    assert checkmd5.make_hash(locate_data(input_file), algo='sha384') == output

@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha512')
)
def test_sha512_hash(input_file, output):
    assert checkmd5.make_hash(locate_data(input_file), algo='sha512') == output

def test_IOError():
    with pytest.raises(IOError):
        checkmd5.make_hash('fake_file.txt')

@pytest.mark.parametrize(
    'algo',
    ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
)
def test_cli_script(algo):
    args = shlex.split('md5checker ./tests/data/file1.txt -a ' + algo)
    if '2.6' not in PYTHON_VERSION:
        res = subprocess.check_output(args).decode('utf-8').strip()
        assert res == FILES['file1'][algo]
    else:
        res = make_regression_call_to_cli(args)
        assert res == FILES['file1'][algo]

@pytest.mark.parametrize(
    'args',
    ['md5checker', 'md5checker 1 2 3 4']
)
def test_cli_with_incorrect_args( args):
    args = shlex.split('md5checker')
    if '2.6' not in PYTHON_VERSION:
        res = subprocess.check_output(args).strip().decode('utf-8')
        assert res == USAGE_PROMPT
    else:
        res = make_regression_call_to_cli(args)
        assert res == USAGE_PROMPT

def test_get_version():
    args = shlex.split('md5checker -v')
    if '2.6' not in PYTHON_VERSION:
        res = subprocess.check_output(args).strip().decode('utf-8')
        assert res == VERSION
    else:
        res = make_regression_call_to_cli(args)
        assert res == VERSION

def test_list_algorithms():
    args = shlex.split('md5checker -a')
    if '2.6' not in PYTHON_VERSION:
        res = clean_output(subprocess.check_output(args).decode('utf-8').strip())
        assert res == ALGOS
    else:
        res = clean_output(make_regression_call_to_cli(args))
        assert res == ALGOS

def test_wrong_option_flags():
    args = shlex.split('md5checker fake_file.txt -b foption')
    if '2.6' not in PYTHON_VERSION:
        res = clean_output(subprocess.check_output(args).decode('utf-8').strip())
        assert res == OPTIONAL_FLAGS
    else:
        res = clean_output(make_regression_call_to_cli(args))
        assert res == OPTIONAL_FLAGS

def make_regression_call_to_cli(args):
    ''' return tuple (stdout, stderr) '''
    return subprocess.Popen(args, stdout=PIPE).communicate()[0].strip()

def locate_data(input_file):
    return _join('tests', 'data', input_file)

def clean_output(output):
    return output.replace('\r', '')
