'''
输入三角形三条边，判断是否构成三角形
计算三角形周长、面积
'''
import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a + b > c and a + c > b and b + c > a:

    print('三角形周长为：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('三角形面积为：%f' % area)

else:
    print('不能构成三角形')