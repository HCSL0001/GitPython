import time

def introduction():
    print("欢迎来到童话冒险游戏！")
    print("你是一个勇敢的骑士，你的任务是解救被邪恶巫师困住的公主。")
    print("你需要通过战斗、解密和探索来完成你的任务。")
    print("祝你好运！")
    print()

def choose_weapon():
    weapon = ""
    while weapon != "剑" and weapon != "锤子" and weapon != "弓箭":
        weapon = input("请选择你的武器(剑/锤子/弓箭)：")
    return weapon

def battle(weapon):
    print("你遇到了一只凶恶的怪物！")
    print("你拔出你的" + weapon + "准备战斗。")
    time.sleep(1)
    print("战斗开始！")
    time.sleep(1)
    if weapon == "剑":
        print("你挥舞着剑，猛烈地攻击怪物。")
        time.sleep(1)
        print("你成功击败了怪物，继续前进。")
    elif weapon == "锤子":
        print("你挥舞着锤子，砸向怪物。")
        time.sleep(1)
        print("怪物受到重击，倒在了地上。你继续前进。")
    elif weapon == "弓箭":
        print("你拿起弓箭，瞄准怪物并射出。")
        time.sleep(1)
        print("箭矢命中怪物要害，它倒下了。你继续前进。")

def puzzle():
    print("你来到了一扇巨大的门前。门上有三个按钮，上面刻着数字1，2，3。")
    print("你需要按照正确的顺序按下按钮才能打开门。")
    time.sleep(1)
    correct_sequence = [3,1,2]
    player_sequence =[]
    while player_sequence != correct_sequence:
        player_sequence = []
        for i in range(3):
            player_sequence.append(int(input("请输入第" + str(i + 1) + "个按钮数字：")))
        if player_sequence != correct_sequence:
            print("错误的顺序！请重试。")
    print("你按下了正确的按钮顺序，门打开了。你继续前进。")

def explore():
    print("你在森林中探险。")
    print("你发现了一条小路，你决定沿着它走。")
    time.sleep(1)
    print("在小路的尽头，你发现了一个隐藏的宝藏！")
    print("你获得了宝藏中的财宝。")
    print("你继续前进，离公主越来越近。")

def rescue_princess():
    print("你来到了巫师的城堡。")
    print("你成功解救了被困的公主！")
    print("公主非常感激地和你一起返回王国。")
    print("你完成了你的任务，取得了胜利！")
    print("恭喜你，勇敢的骑士！")

# 游戏主循环
def game_loop():
    introduction()
    weapon = choose_weapon()
    battle(weapon)
    puzzle()
    explore()
    rescue_princess()

game_loop()