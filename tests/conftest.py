import pytest
import os
import json

DIRECTORY = os.path.dirname(__file__)
_join = os.path.join
DATA_PATH = os.path.abspath(_join(DIRECTORY, 'data'))


@pytest.fixture(scope='module')
def files():
    ''' Available to other test modules as files object '''
    with open(str(_join(DATA_PATH, 'data.json')), 'r') as f:
        return json.loads(f.read())
