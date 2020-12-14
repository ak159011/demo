import pickle

# name=['张三','李四','王五']
# file=open('name_a.txt',mode='wb')
# a_name=pickle.dump(name,file)
# file.close()
file1 = open('name_a.txt', mode='rb')
name_a = pickle.load(file1)
print(name_a)
file1.close()
# b_anme=pickle.dumps(name)
#
# file=open('name.txt',mode='wb')
# file.write(b_anme)
# file.close()

# file1=open('name.txt',mode='rb')
# x=file1.read()
# y=pickle.loads(x)
# print(y)
# file1.close()
