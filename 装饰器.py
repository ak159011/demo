import time

# def zsq(fn):
#     def a():
#         start = time.time()
#         fn()
#         end = time.time()
#         print(end - start)
#     return a
# @zsq
# def foo():
#     y = 1
#     for i in range(1, 10000) :
#         y *= i
#
#     print(y)
#
#
# foo()
user = 8
r = 8
w = 4
d = 2
e = 1


def prs(x, y):
    def i(fn):
        def p():
            if x&y!=0:
                fn()
            else:
                print('没有权限')

        return p #函数i的返回值
    return i     #函数p的返回值


@prs(user, r)
def read() :
    print('读数据')


@prs(user, w)
def write() :
    print('写数据')


@prs(user, d)
def delete() :
    print('读数据')


@prs(user, e)
def exec() :
    print('读数据')


read()
write()
delete()
exec()
