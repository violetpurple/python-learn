'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
             玩家第一次如果摇出2点、3点或12点，庄家胜；
             其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
             其他点数，玩家继续要骰子，直到分出胜负。
'''

from random import randint

money = 1000
# 主循环，当资产大于零，重新下注开始下一局
while money > 0:

    print('你的资产：' , money)
    
    # 子循环，先下注，按照游戏规则顺序执行，知道分出胜负
    while True:
        # 下注金额
        debt = int(input("请下注："))
        if 0 < debt <= money:
            break

    # 摇色子，记录点数
    first = randint(1, 6) + randint(1, 6)
    print("你摇出的点数：%d" % first)
    # 玩家胜 资产加上下注金额，否则减去下注金额
    # 7或者11点，玩家胜
    needs_go_on = False
    if first == 7 or first == 11:
        money += debt
        print("玩家胜")
    # 2/3/12点，庄家胜
    elif first == 2 or first == 3 or first == 12:
        money -+ debt
        print("庄家胜")
    else:
        needs_go_on = True

    # 循环，继续摇色子，7点，庄家胜，第一次点数，玩家胜，其他点数循环
    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print("玩家摇出了%d 点" % current)
        if current == 7:
            money -= debt
            needs_go_on = False
            print("庄家胜")
        elif current == first:
            money += debt
            print("玩家胜")
            needs_go_on = False

# 提示游戏结果        
print("你失败了，游戏结束")


