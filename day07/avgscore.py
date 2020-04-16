"""
输入学生考试成绩计算平均分
"""

def main():
    
    number = int(input("请输入学生人数："))
    names = [None] * number
    scores = [None] * number
    
    for index in range(len(names)):
        names[index] = input("请输入第【%d】个学生的姓名：" % (index + 1))
        scores[index] = float(input("请输入第【%d】个学生的成绩：" % (index + 1)))
    
    totalScore = 0

    for index in range(len(names)):
        print("%s: %.1f 分" % ( names[index], scores[index]))
        totalScore += scores[index]

    print("平均分为： %.1f" % (totalScore / number))


if __name__ == "__main__":
    main()
