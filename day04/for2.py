'''
用for循环实现1到100之间的偶数求和
'''

sum = 0

for i in range(2, 101, 2):
    sum += i
print('1到100之间偶数的合是：%d' % sum)    
