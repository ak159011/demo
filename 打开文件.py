# # 1.写入数据
# file=open('b.txt',mode='w',encoding='utf-8')
# file.write('床前明月光\n')
# file.write('疑是地上霜\n')
# file.write('举头望明月\n',)
# file.write('低头思故乡\n')
# file.close()
# 2.读取文件
file=open('b.txt',mode='r',encoding='utf-8')
con=file.readlines()
for i in con:
    print(i)
file.close()
