import hashlib


def jiami(passwd) :
    h = hashlib.sha256()
    h.update(passwd.encode('utf8'))
    y=h.hexdigest()
    return y

y=jiami('wdwqdqwdqwd')
print(y)
