''' Constants used throughout test modules '''
import hashlib
import md5checker
import json
import os
import platform
import subprocess

join = os.path.join
_algorithms = sorted(list(hashlib.algorithms_guaranteed))
_prompt = 'Available hash types\n'
_response = _prompt + ('-' * len(_prompt)) + '\n\n' + '\n'.join(_algorithms)
ALGOS = _response
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
