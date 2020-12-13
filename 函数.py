def kk (m):
    sum=1
    for i in range(1,m+1):
        sum*=i
    return sum

def hh(n):
    i=0
    for x in range(1,n+1):
        i+=kk(x)
    return i


print(hh(5))