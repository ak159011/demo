print('-----------------------------')
print('     ', '名片管理系统v1.0')
print('1:添加名片')
print('2:删除名片')
print('3:修改名片')
print('4:查询名片')
print('5:显示所有名片')
print('6:退出系统')
print('-----------------------------')

flage = True
a = []
b = {}
def add():
    global b
    global a
    name = input('请输入姓名：')
    if name not in b.values():
        xb = input('请输入性别：')
        age = input('请输入年龄：')
        Tel = input('请输入电话号码：')

        b = {'姓名': name, '性别': xb, '年龄': age, '电话号码': Tel}

        a.append(b)
    else:
        flage = True

def rm():
    global a
    index = int(input('请输入要删除的序号：'))
    a.remove(a[index])

def change():
    global b
    global a
    c = {}
    index1 = int(input('请输入要修改的序号'))
    print('序号', '姓名', '性别', '年龄', '电话号码')
    print(a.index(a[index1]), a[index1].get('姓名'), a[index1].get('性别'), a[index1].get('年龄'), a[index1].get('电话号码'),
          sep='    ')
    name = input('请输入姓名：')
    if name not in b.values():
        xb = input('请输入性别：')
        age = input('请输入年龄：')
        Tel = input('请输入电话号码：')
        c = {'姓名': name, '姓名': xb, '年龄': age, '电话号码': Tel}
        x = a[index1]
        x.clear()
        x.update(c)

def find():
    global a
    name = input('请输入查找的姓名：')
    for n in a:
        # print(n)
        m = n.get('姓名')
        if m == name :
            print(n.get('姓名'), n.get('姓名'), n.get('年龄'), n.get('电话号码'))
        else:
            print('没有找到')
            flage = True

def look():
    global a
    q = 0
    print('序号', '姓名', '性别', '年龄', '电话号码')
    while q < len(a):

        print(a.index(a[q]), a[q].get('姓名'), a[q].get('性别'), a[q].get('年龄'),
              a[q].get('电话号码'), sep='    ')
        q += 1
    else:
        flage = True

def start():
    global flage
    while flage:
        i = int(input('请输入数字操作名片：'))
        if i == 1:
            add()
        if i == 2:
            rm()
        if i == 3:
            change()
        if i == 4:
            find()
        if i == 5:
            look()
        if i == 6:
            flage = False

if __name__ == '__main__':
    start()

