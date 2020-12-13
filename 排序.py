a = [7, 2, 4, 2, 9, 0, 1, '']

for i in a:
    if i == '':
        a.remove(i)
print(a)

# x = a[0]
# for i in a :
#     if i > x :
#         x = i
# print(x)
# print(a.index(x))
# print(i)
'''冒泡排序'''
# j=0
# while j < len(a) :
#     j += 1
#     i = 0
#     c = 0
#     while i < len(a) - 1 -i:
#         if a[i] > a[i + 1] :
#             c = a[i]
#             a[i] = a[i + 1]
#             a[i + 1] = c
#         i += 1
# print(a)

# j = 0
# while j < len(a) :
#     j+=1
#     i = 0
#     while i < len(a) - 1 :
#
#         if a[i] > a[i + 1] :
#             a[i], a[i + 1] = a[i + 1], a[i]
#         i += 1
#
# print(a)
