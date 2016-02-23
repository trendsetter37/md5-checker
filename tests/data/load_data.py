''' Used to load data files '''
#from random_words import RandomWords
import json
import hashlib
from md5checker import make_hash
import os

DIR = os.path.dirname(__file__)
_join = os.path.join

hashes = [algo for algo in hashlib.algorithms_guaranteed]

'''
rw = RandomWords()

for x in xrange(1, 11):
    with open('file' + str(x) + '.txt', 'wb') as f:
        words = rw.random_words(count=10)
        f.write(str(' '.join(words)))
'''

def append_hashes():
    json_file = open('data.json', 'r')
    files = json.load(json_file)
    for file_key in files.keys():
        for h in hashes:
            # Add rel path to input file
            files[file_key]['input_file'] = file_key + '.txt'
            files[file_key][h] = make_hash(file_key + '.txt', algo=h)

    json.dump(
        files,
        open('data.json', 'w'),
        sort_keys=True,
        separators=(',', ':'),
        indent=4
    )

    json_file.close()
if __name__ == '__main__':
    append_hashes()
