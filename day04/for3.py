'''
计算非负整数n的阶乘
'''

n = int(input('n='))
result = 1

for i in range(1, n):
    result *= i
print('n! = %d' % result)    
