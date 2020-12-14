# for...in 的本质是调用对象的__iter_方法，然后再调用__next__将数据取出
# 使用迭代器实现斐波拉契数列
"""
y:表示第几个数
"""


class fb(object) :
    def __init__(self, y) :
        self.y = y
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self) :
        return self

    def __next__(self) :
        if self.count <= self.y :
            self.count += 1
            x = self.num1
            self.num1, self.num2 = self.num2, self.num2 + self.num1
            return x
        else :
            raise StopIteration


d = fb(100)
for i in d :
    print(i)
