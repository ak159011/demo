def div(a, b):
    try:
        x = a / b
    except  Exception as e:
        print('程序出错了')
    else:
        print(x)


div(1, 0)
