''' Test command line functionality '''
import pytest
import shlex
import sys
from .__init__ import *


class TestCLI(object):
    # Ensure that the package is installed for this to work
    @pytest.mark.parametrize(
        'algo',
        ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    )
    def test_cli_script(self, algo):
        args = shlex.split(
            'md5checker ' + 'tests/data/file1.txt' + ' -a ' + algo
        )
        expected = FILES['file1'][algo]
        if '2.6' not in PYTHON_VERSION:
            res = subprocess.check_output(args).decode('utf-8').strip()
            assert res == expected
        else:
            res = TestCLI.make_regression_call_to_cli(args)
            assert res == expected

    def test_list_algorithms(self):
        args = shlex.split('md5checker -a')
        if '2.6' not in PYTHON_VERSION:
            res1 = md5checker.list_algorithms()
            assert res1 == ALGOS
        else:
            res1 = md5checker.list_algorithms()
            assert res1 == ALGOS_26

    def test_main_invocation(self):
        # fill sys.argv with vars from test_cli module
        print('Pseudo args are: ')
        print(len(sys.argv))

    @staticmethod
    def make_regression_call_to_cli(args):
        ''' return tuple (stdout, stderr) '''
        return subprocess.Popen(args, stdout=PIPE).communicate()[0].strip()

    @staticmethod
    def clean_output(output):
        return output.replace('\r', '')
