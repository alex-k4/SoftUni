# 1
# mark = float(input())
# if mark >= 5.50:
#     print("Excellent!")

# 2
# number1 = int(input())
# number2 = int(input())
#
# if number1 > number2:
#     print(number1)
# else:
#     print(number2)

# 3
# number = int(input())
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

# 4
# number = int(input())
#
# if number < 100:
#     print("Less than 100")
# elif 100 <= number <= 200:
#     print("Between 100 and 200")
# elif number > 200:
#     print("Greater than 200")

# 5
# password = input()
#
# if password == "s3cr3t!P@ssw0rd":
#     print("Welcome")
# elif password != "s3cr3t!P@ssw0rd":
#     print("Wrong password!")

# 6
# from math import pi
# figure = input()
#
# if figure == "square":
#     a = float(input())
#     area = a * a
#     print(f"{area:.3f}")
# elif figure == "rectangle":
#     a = float(input())
#     b = float(input())
#     area = a * b
#     print(f"{area:.3f}")
# elif figure == "circle":
#     r = float(input())
#     area = pi * (r * r)
#     print(f"{area:.3f}")
# elif figure == "triangle":
#     a = float(input())
#     h = float(input())
#     area = (a * h) / 2
#     print(f"{area:.3f}")

# 7
# price_for_excursion = float(input())
# puzzle_count = int(input())
# doll_count = int(input())
# teddy_bear_count = int(input())
# minion_count = int(input())
# truck_count = int(input())
#
# puzzle = 2.60
# doll = 3
# teddy_bear = 4.10
# minion = 8.20
# truck = 2
#
# profit = puzzle * puzzle_count + doll * doll_count + teddy_bear * teddy_bear_count \
#     + minion * minion_count + truck * truck_count
#
# count_all = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count
#
# if count_all >= 50:
#     discount = 25/100 * profit
#     profit = profit - discount
#
# profit_left_after_rent = profit - 10/100 * profit
#
# if profit_left_after_rent >= price_for_excursion:
#     left_money = profit_left_after_rent - price_for_excursion
#     print(f"Yes! {left_money:.2f} lv left.")
# elif price_for_excursion > profit_left_after_rent:
#     needed_money = price_for_excursion - profit_left_after_rent
#     print(f"Not enough money! {needed_money:.2f} lv needed.")






