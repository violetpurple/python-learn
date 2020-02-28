import math

radius = float(input('请输入圆的半径：'))
peremeter = 2 * math.pi * radius
area = math.pi * radius * radius

print('圆的半径长%.2f，周长%.2f，面积%.2f' %(radius, peremeter, area))
