class fz(object) :
    def __init__(self, mj, jj=None):
        if jj is None :
            jj = []
        self.mj = mj
        self.kmj = mj * 0.3
        self.jj = jj

    def add(self,x):
       if self.kmj<x.mj:
           print('jjl')
       else:
           self.jj.append(x.name)
           self.kmj-=x.mj
    def __str__(self):
        return ('mj={},kmj={},jj={}'.format(self.mj,self.kmj,self.jj))
    @staticmethod
    def a():
        print('ddd')
    @classmethod
    def b(cls):
        pass

class jj(object):
    def __init__(self,name,mj):
        self.name=name
        self.mj=mj


bed=jj('bed',6)
gg=jj('gg',5)

a=fz(50)
a.add(bed)
a.add(gg)
print(a)


print(dir(a))