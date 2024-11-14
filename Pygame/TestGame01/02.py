# 游戏开始
print("欢迎来到文字冒险游戏！")
print("你醒来在一个陌生的房间里，门是开着的。")

# 玩家输入选择
choice = input("你想做什么？(1.开门 2.查看房间):")

if choice == "1":
    print("你走出房间，发现自己在一片森林中。")
    print("你有两个选择：")
    print("1.沿着小路走")
    print("2.进入森林深处")
    path_choice = input("请输入你的选择：")
    if path_choice == "1":
        print("你沿着小路走，遇到了一只小兔子。")
        print("你有两个选择：")
        print("1.抓住小兔子")
        print("2.离开小兔子")
        rabbit_choice = input("请输入你的选择：")
        if rabbit_choice == "1":
            print("你抓住了小兔子，它变成了一个钥匙。")
            key = "钥匙"
        else:
            print("你离开了小兔子，继续前进。")
    elif path_choice == "2":
        print("你进入森林深处，遇到了一只大熊。")
        print("你有两个选择：")
        print("1.逃跑")
        print("2.战斗")
        bear_choice = input("请输入你的选择：")
        if bear_choice == "1":
            print("你成功逃跑，继续前进。")
        elif bear_choice == "2":
            print("你选择战斗，与大熊展开了激战。")
            # 战斗逻辑
            # ...
        else:
            print("无效的选择，游戏结束。")
    else:
        print("无效的选择，游戏结束。")
else:
    print("你选择留在房间，游戏结束。")