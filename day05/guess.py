'''
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
'''

import randint from random

answer = randint.randint(1, 100)
count = 0

while True:
    count += 1
    number = int(input("请输入你的数字："))
    if number > answer:
        print("数字大了")
    elif number < answer
        print("数字小了")
    else:
        print("答对了")
        break

print("你总共猜了%d次" % count)    
if count > 7 :
    print("你的智商需要充值")
