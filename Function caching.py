import time
from functools import lru_cache

@lru_cache(maxsize=4)
def someWork(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Call 1")
    someWork(3)
    someWork(1)
    someWork(2)
    someWork(4)
    print("Call 2")
    someWork(3)
    someWork(1)
    someWork(2)
    someWork(4)
    print("Call 3")