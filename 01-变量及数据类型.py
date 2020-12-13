import random
x=10
y=1
while x>y:

 a = int(input('请输入剪刀0，石头1，布2: '))
 print('用户出的是', a)
 b = random.randint(0, 2)
 print('电脑出的是', b)
 if (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1):
  print('you win')
 elif(a==b):
  print('平局')
 else:
  print('you lose')
 y+=1

print(random.randrange(0, 20, 2))