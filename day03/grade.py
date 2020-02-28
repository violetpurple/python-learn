"""
分数登记映射

分数>=90, A
80 =< 分数 <90 , B
70 =< 分数 < 80, C
60 =< 分数 < 70, D
分数 < 60, E
"""

score = int(input('请输入分数：'))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('等级是：', grade)                    