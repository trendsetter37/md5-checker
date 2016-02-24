0.2.0
=====
* Added Tests

* Added support for additional Hash algorithms
  * sha1
  * sha224
  * sha256
  * sha384
  * sha512

* Add command line algorithms List


0.1.1
=====
* Clerical fixes
* `Argument checking`_



Argument checking
-----------------
::

  def main():
      ''' Entry point for the application script '''
      args = sys.argv
      if len(args) != 2:
          print('Usage: md5checker "path-to-file"')
      else:
          print(make_hash(sys.argv[1]))



0.1.0
==============

* Added hash function for single files.
