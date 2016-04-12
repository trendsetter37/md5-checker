''' Constants used throughout test modules '''
import hashlib
import md5checker
import json
import os
import platform
import subprocess
import sys

join = os.path.join

ALGOS = tuple(sorted(list(hashlib.algorithms_guaranteed)))
ALGOS_26 = (
    'MD5', 'SHA1', 'SHA224',
    'SHA256', 'SHA384', 'SHA512'
)
CHECKMD5 = md5checker.checkmd5
CLI = md5checker
DIRECTORY = os.path.dirname(__file__)
DATA_PATH = os.path.abspath(join(DIRECTORY, 'data'))
FILES = json.loads(open(join(DATA_PATH, 'data.json'), 'r').read())
OPTIONAL_FLAGS = 'Optional flags are -a or --algo'
PIPE = subprocess.PIPE
PYTHON_VERSION = platform.python_version()  # Check for python 2.6
SYSTEM = platform.system()
USAGE_PROMPT = 'Usage: md5checker "path-to-file" [options]'
VERSION = md5checker.__version__
