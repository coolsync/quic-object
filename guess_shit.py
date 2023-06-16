# 3 18
# 0 < total < 10 -> big
# 10 < total < 19 -> small
import random

# def print_info(point_list, result_info):

# flag = True
# for _ in range(3):
#     print("<<<Game starts>>>")
#     total_str = input("Big or small\n")
#     point1 = random.randrange(1, 7)
#     point2 = random.randrange(1, 7)
#     point3 = random.randrange(1, 7)

#     point_list = [point1, point2, point3]

#     total = sum(point_list)
#     print("<<<Role the dice>>>")
#     if (total_str == "small") and (0 < total < 11):
#         print(f"{point_list}, 'you lose'")
#     elif total_str == "big" and 10 < total < 19:
#         print(f"{point_list}, 'you win'")


def roll_points(times=3, points=None):
    if points is None:
        points = []
    while True:
        if times <= 0:
            break
        points.append(random.randrange(1, 7))
        # print(f'{random.randrange(1,7)}')
        times = times - 1
    # print(points)
    return points


def roll_results(total):
    isSmall = 1 <= total <= 10
    isBig = 11 <= total <= 18

    if isBig:
        return "Big"
    else:
        return "Small"


def start_game():
    print("<<<  Game Start  >>>")
    # 1.
    choices = ["Big", "Small"]
    points = roll_points()
    your_choice = input("Big or Small: \n")
    if your_choice in choices:
        youWin = your_choice == roll_results(sum(points))
        if youWin:
            print(f"your points: {points}, you win")
        else:
            print(f"your points: {points}, you lose")
    else:
        print("invalid words")
        start_game()


# start_game()


# 初始金额： 1000
# 金额为0时 游戏结束
# 默认赔率为1倍
def roll_results2(total):
    isSmall = 1 <= total <= 10
    isBig = 11 <= total <= 18
    if isBig:
        return "Big"
    else:
        return "Small"


def play():
    origin_money = 1000
    while True:
        rest_money = 0
        you_bet = int(input("you bet: "))
        # rest_money = origin_money - you_bet
        points = roll_points()
        choices = ["Big", "Small"]
        your_choice = input("Big or Small: \n")
        if your_choice in choices:
            you_win = your_choice == roll_results(sum(points))
            if you_win:
                print(f"your points: {points}, you win")
                rest_money = you_bet + origin_money
                print(f"you gaind {you_bet}, you now have {rest_money}")
            else:
                print(f"your points: {points}, you lose")
                rest_money = origin_money - you_bet
                print(f"you lose {you_bet}, you now have {rest_money}")

            if rest_money == 0:
                print("you lose done, play end")
                break
        else:
            print("invilad words")
            play()


play()
#####
# you bet: 10
# Big or Small:
# Big
# your points: [4, 1, 5], you lose
# you lose 10, you now have 990
# you bet: 100
# Big or Small:
# small
# invilad words
# you bet: 100
# Big or Small:
# Small
# your points: [1, 4, 6], you lose
# you lose 100, you now have 900
# you bet: 50
# Big or Small:
# Small
# your points: [1, 6, 1], you win
# you gaind 50, you now have 1050
#####
