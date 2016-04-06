''' Constants used throughout test modules '''
import md5checker
import json
import os
import platform
import subprocess

join = os.path.join
ALGOS = """Available hash types
--------------------

md5
sha1
sha224
sha256
sha384
sha512"""
CHECKMD5 = md5checker.checkmd5
DIRECTORY = os.path.dirname(__file__)
DATA_PATH = os.path.abspath(join(DIRECTORY, 'data'))
FILES = json.loads(open(join(DATA_PATH, 'data.json'), 'r').read())
OPTIONAL_FLAGS = 'Optional flags are -a or --algo'
PIPE = subprocess.PIPE
PYTHON_VERSION = platform.python_version()  # Check for python 2.6
SYSTEM = platform.system()
USAGE_PROMPT = 'Usage: md5checker "path-to-file" [options]'
VERSION = md5checker.__version__
