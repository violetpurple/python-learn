'''
输出2~99之间的素数
'''

import math

for num in range(2, 1000):
    isPrime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            isPrime = False
            break
    if isPrime == True:
        print(num, end="  ")

    