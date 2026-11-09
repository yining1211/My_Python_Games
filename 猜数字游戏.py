import random
def start_guess(min,max):
    is_guess=random.randint(min, max)
    new_min=min
    new_max=max
    print(f"范围在{min}-{max}之间")
    for i in range(10):
        try:
            your_guess=int(input("请输入你要猜的数字"))
        except:
            print("请输入有效数字")
            continue
        if your_guess==is_guess:
            print(f"你在第{i+1}次猜对了，数字是{your_guess}")
            break
        else:
                if your_guess<is_guess:
                    new_min=your_guess
                    print(f"猜小了，范围在{new_min}-{new_max}之间")
                else:
                    new_max=your_guess
                    print(f"猜大了，范围在{new_min}-{new_max}之间")
    print("游戏结束，请下次再玩^_^")
    input("按回车键退出^_^")
min1=int(input("请输入一个最小值"))
max1=int(input("请输入一个最大值"))
A=start_guess(min1,max1)
