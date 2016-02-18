''' Testing MD5 functionality '''
from data.data import files
from md5checker import make_hash

def test_md5_hash():
    for obj in files.keys():
        filename = 'tests/data/' + obj + '.txt'
        assert files[obj]['md5'] == make_hash(filename).upper()
