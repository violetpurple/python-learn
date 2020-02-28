'''
输入行数打印三角形
'''

row = int(input('请输入行数: '))

'''
#循环打印从1到row
for i in range(row):
    for j in range(i + 1):
        print(j + 1, end='')
    print()
'''

#循环打印星号
for i in range(row):
    for j in range(i + 1):
        print('*', end='')
    print()
'''

#倒循环打印
for i in range(row):
    for j in range(row):
        if  (j + 1) < (row - i):
            print(j + 1, end='')
        else:
            print('*', end='')
    print()
'''

#到循环打印星号
for i in range(row):
    for j in range(row):
        if  (j + 1) < (row - i):
            print(' ', end='')
        else:
            print('*', end='')
    print()
'''

#居中循环打印
for i in range(row):
    for j in range( row + i):
        if  (j + 1) < (row - i):
            print(j + 1, end='')
        else:
            print('*', end='')
    print()
'''

#居中循环打印星号
for i in range(row):
    for j in range( row + i):
        if  (j + 1) < (row - i):
            print(' ', end='')
        else:
            print('*', end='')
    print()


