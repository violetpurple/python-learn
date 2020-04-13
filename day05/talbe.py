'''
输出乘法口诀表(九九表)
'''

for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print("%d * %d = %d" %(j, i, i * j), end="  ")
    print("", end='\n')
