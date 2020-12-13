import csv

file = open('test.csv', 'w', encoding='utf8', newline='')
w = csv.writer(file)
w.writerow(['name', 'age', 'xbie', 'city'])
w.writerow(['hh', 12, '女', '日本'])
file.close()


file = open('test.csv', 'r', encoding='utf8')
w=csv.reader(file)

for i in w:
    print(i)


