.. image:: https://travis-ci.org/trendsetter37/md5-checker.svg?branch=master
   :target: https://travis-ci.org/trendsetter37/md5-checker
   :width: 50%

.. image:: https://codecov.io/github/trendsetter37/md5-checker/coverage.svg?branch=master
   :target: https://codecov.io/github/trendsetter37/md5-checker?branch=master
   :width: 50%


MD5Checker
==========

This module is a simple utility to examine a file's checksum

Install
-------

One-liner
~~~~~~~~~
::

  pip install md5checker

Other ways
~~~~~~~~~~~
::

  git clone https://github.com/trendsetter37/md5-checker
  cd md5-checker

Followed by:

::

  python setup.py install

or

::

  pip install .

Testing (Development)
---------------------

Inside the root directory, run


::

  pip install -r requirements.txt
  pip install -e .
  py.test

or

::

  pip install -r requirements.txt
  pip install -e .
  python setup.py test

Usage
-----

Command Line
~~~~~~~~~~~~
::

  md5checker "Space containing directory/path-to-file.extension"

Surround path with double quotes if it contains spaces. Otherwise
quotations are unnecessary.

::

  md5checker space-containing-directory/path-to-file.extension

Module
~~~~~~
::

  >>> from md5checker import make_hash
  >>> make_hash('test2.txt')
  '970d8d13fc40ecb5c382790540d227a4'
  >>>
