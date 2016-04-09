''' Test command line functionality '''
import pytest
import shlex
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
        if '2.6' not in PYTHON_VERSION:
            res = subprocess.check_output(args).decode('utf-8').strip()
            expected = FILES['file1'][algo]
            assert res == expected
        else:
            res = TestCLI.make_regression_call_to_cli(args)
            assert res == expected

    @pytest.mark.parametrize(
        'args',
        ['md5checker', 'md5checker 1 2 3 4']
    )
    def test_cli_with_incorrect_args(self, args):
        args = shlex.split('md5checker')
        if '2.6' not in PYTHON_VERSION:
            res = subprocess.check_output(args).strip().decode('utf-8')
            res1 = md5checker.usage()
            assert res == USAGE_PROMPT
            assert res1 == USAGE_PROMPT
        else:
            res = TestCLI.make_regression_call_to_cli(args)
            res1 = md5checker.usage()
            assert res == USAGE_PROMPT
            assert res1 == USAGE_PROMPT

    def test_get_version(self):
        args = shlex.split('md5checker -v')
        if '2.6' not in PYTHON_VERSION:
            res = subprocess.check_output(args).strip().decode('utf-8')
            res1 = md5checker.__version__
            assert res == VERSION
            assert res1 == res
        else:
            res = TestCLI.make_regression_call_to_cli(args)
            res1 = md5checker.__version__
            assert res == VERSION
            assert res1 == res

    def test_list_algorithms(self):
        args = shlex.split('md5checker -a')
        if '2.6' not in PYTHON_VERSION:
            res = TestCLI.clean_output(
                subprocess.check_output(args).decode('utf-8').strip()
            )
            res1 = md5checker.list_algorithms()
            assert res == ALGOS
            assert res1 == res
        else:
            res = TestCLI.clean_output(
                TestCLI.make_regression_call_to_cli(args)
            )
            res1 = md5checker.list_algorithms()
            assert res == ALGOS_26

    def test_wrong_option_flags(self):
        args = shlex.split('md5checker fake_file.txt -b foption')

        if '2.6' not in PYTHON_VERSION:
            res = TestCLI.clean_output(
                subprocess.check_output(args).decode('utf-8').strip()
            )
            assert res == OPTIONAL_FLAGS
        else:
            res = TestCLI.clean_output(
                TestCLI.make_regression_call_to_cli(args)
            )
            assert res == OPTIONAL_FLAGS

    @staticmethod
    def make_regression_call_to_cli(args):
        ''' return tuple (stdout, stderr) '''
        return subprocess.Popen(args, stdout=PIPE).communicate()[0].strip()

    @staticmethod
    def clean_output(output):
        return output.replace('\r', '')
