.. image:: https://travis-ci.org/trendsetter37/md5-checker.svg?branch=master
    :target: https://travis-ci.org/trendsetter37/md5-checker

MD5Checker
==========

This module is a simple utility to examine a file's checksum

Install
-------
::

    pip install md5checker


Usage
-----

Command Line
^^^^^^^^^^^^
::

    md5checker "Space containing directory/path-to-file.extension"

Surround path with double quotes if it contains spaces.

Module
^^^^^^
::

    >>> from md5checker import make_hash
    >>> make_hash('test2.txt')
    '970d8d13fc40ecb5c382790540d227a4'
    >>>
