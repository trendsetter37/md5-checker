from setuptools import setup
import md5checker

setup(
    name='md5check',
    version=md5checker.__version__,
    description='Check file md5 hashes',
    long_description=open('README.rst').read(),
    url='http://github.com/trendsetter37/md5checker',
    license=md5checker.__license__,
    author=md5checker.__author__,
    author_email='javissullivan@gmail.com',
    packages=[
        'md5checker',
    ],
    entry_points={
        'console_scripts': [
            'md5checker = md5checker.checkmd5.make_file_hash',
        ],
    },

    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities',
    ],
)
