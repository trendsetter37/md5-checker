''' Used to load data files '''
from random_words import RandomWords

rw = RandomWords()

for x in xrange(1, 11):
    with open('file' + str(x) + '.txt', 'wb') as f:
        words = rw.random_words(count=10)
        f.write(str(' '.join(words)))
