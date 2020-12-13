import time

def zsq(fn):
    def a():
        start = time.time()
        fn()
        end = time.time()
        print(end - start)
    return a
@zsq
def foo():
    y = 1
    for i in range(1, 10000) :
        y *= i

    print(y)


foo()