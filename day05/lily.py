''' 计算100-999之间的水仙花数
     三位数各位数字三次方之和等于数字本身
'''

for num in range(100, 1000) :
    low = num % 10
    mid = num //10 % 10
    hig = num // 100
    if num == low ** 3 + mid ** 3 + hig ** 3 :
        print(num)
