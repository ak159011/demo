def add(n):
    if n==0:
        return 0
    return n+add(n-1)


print(add(5))


#阶乘n!=n*(n-1)

def jc(n):
    if n==0:
        return 1

    return n*jc(n-1)
print(jc(5))

#斐波拉契数列的第n个数
def fblq(n):
    if n==1 or n==2:
     return 1
    return fblq(n-2)+fblq(n-1)


print(fblq(8))