"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""

num = int(input("请输入数字："))
reversedNum = 0
temp = num

while temp > 0:
    # 取最低位数字 + 回文数
    reversedNum = reversedNum * 10 + temp % 10
    # 临时数取整
    temp = temp // 10

print("输入数字为%d， 反转后数字为 %d 。" % (num, reversedNum))
if reversedNum == num :
    print("%d 是回文数" % num)     
else:
    print("%d 不是回文数" % num)     
