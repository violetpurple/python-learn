'''
输入一个正整数判断是不是素数
'''

from math import sqrt

num = int(input('请输入正整数：'))
end = int(sqrt(num))
is_prime = True

for i in range(2, end + 1):
    if num % i ==0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d是素数' % num)    
else:
    print('%d不是素数' % num)    
