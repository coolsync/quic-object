import random

ORIGIN_NUMBER = 1000
CHOICES = ["Big", "Small"]

# def roll_points():
#     """投掷骰子，返回两个点数之和"""
#     return random.randint(1, 6) + random.randint(1, 6)

# def roll_results(points):
#     """判断点数结果是“大”还是“小”，返回一个字符串"""
#     return "Big" if points >= 11 else "Small"

# def play():
#     rest_number = ORIGIN_NUMBER
#     while rest_number > 0:
#         you_come = int(input("you come: "))
#         rest_number -= you_come
#         points = roll_points()
#         your_choice = input("Big or Small: \n")
#         if your_choice not in CHOICES:
#             print("invalid words")
#             continue
#         you_resualt = your_choice == roll_results(sum(points))
#         if you_resualt:
#             print(f"your points: {points}, you win")
#             you_come *= 2
#             rest_number += you_come
#             print(f"you gaind {you_come}, you now have {rest_number}")
#         else:
#             print(f"your points: {points}, you lose")
#             print(f"you failed {you_come}, you now have {rest_number}")
#         origin_number = rest_number

# play()


import random
from enum import Enum

class Choices(Enum):
    BIG = "Big"
    SMALL = "Small"

def roll_points():
    """投掷骰子，返回三个点数之和"""
    points = sum([random.randint(1, 6) for _ in range(3)])
    print(f'<<< roll dice >>>\n{points}')
    return points

def roll_results(total):
    """判断点数结果是“大”还是“小”，返回一个字符串"""
    isSmall = 1 <= total <= 10
    isBig = 11 <= total <= 18
    return Choices.BIG.value if isBig else Choices.SMALL.value
    
def play():
    origin_number = 1000
    while origin_number > 0:
        you_come = int(input("you come: "))
        rest_number = origin_number - you_come
        points = roll_points()
        your_choice = input("Big or Small: \n")
        if your_choice in Choices.__members__:
            you_resualt = your_choice == roll_results(points)
            if you_resualt:
                print(f"your points: {points}, you win")
                you_come *= 2
                rest_number = origin_number + you_come
                print(f"you gained {you_come}, you now have {rest_number}")
            else:
                print(f"your points: {points}, you lose")
                print(f"you failed {you_come}, you now have {rest_number}")
        else:
            print("invalid words")
            continue
        origin_number = rest_number

play()
