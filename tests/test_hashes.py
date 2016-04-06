''' Testing MD5 functionality '''
from .__init__ import CHECKMD5, FILES, join
import pytest


def create_parameters(algo):
    return [(FILES[x]['input_file'], FILES[x][algo]) for x in FILES.keys()]


@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('md5')
)
def test_md5_hash(input_file, output):
    assert CHECKMD5.make_hash(locate_data(input_file)) == output


@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha1')
)
def test_sha1_hash(input_file, output):
    assert CHECKMD5.make_hash(locate_data(input_file), algo='sha1') == output


@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha224')
)
def test_sha224_hash(input_file, output):
    assert CHECKMD5.make_hash(locate_data(input_file), algo='sha224') == output


@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha256')
)
def test_sha256_hash(input_file, output):
    assert CHECKMD5.make_hash(locate_data(input_file), algo='sha256') == output


@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha384')
)
def test_sha384_hash(input_file, output):
    assert CHECKMD5.make_hash(locate_data(input_file), algo='sha384') == output


@pytest.mark.parametrize(
    "input_file,output",
    create_parameters('sha512')
)
def test_sha512_hash(input_file, output):
    assert CHECKMD5.make_hash(locate_data(input_file), algo='sha512') == output


def test_IOError():
    with pytest.raises(IOError):
        CHECKMD5.make_hash('fake_file.txt')


def locate_data(input_file):
    return join('tests', 'data', input_file)
