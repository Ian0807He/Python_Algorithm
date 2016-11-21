def fib():
    n1 = 0
    n2 = 1
    yield n1
    while True:
        n1, n2 = n2, n1+n2
        yield n1

import itertools
print(list(itertools.islice(fib(), 10)))
