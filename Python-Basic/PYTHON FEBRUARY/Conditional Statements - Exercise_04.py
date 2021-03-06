# 1
# import math
# time_first = int(input())
# time_second = int(input())
# time_third = int(input())
#
# total_time = time_first + time_second + time_third
#
# minutes = total_time / 60
# seconds = total_time % 60
#
# minutes = math.floor(minutes)
#
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")

# 2
# number = int(input())
# bonus = 0
#
# if number <= 100:
#     bonus += 5
# elif number > 1000:
#     bonus += 0.1 * number
# else:
#     bonus += 0.2 * number
#
#
# if number % 2 == 0:
#     bonus += 1
# elif number % 10 == 5:
#     bonus += 2
#
# print(bonus)
# print(bonus + number)

# 3
# speed = float(input())
#
# if speed <= 10:
#     print("slow")
# elif 10 < speed <= 50:
#     print("average")
# elif 50 < speed <= 150:
#     print("fast")
# elif 150 < speed <= 1000:
#     print("ultra fast")
# else:
#     print("extremely fast")

# 4
# number_to_turn = float(input())
# unit_inp = input()
# unit_output = input()
#
# if unit_inp == "cm":
#     number_to_turn = number_to_turn * 10
# elif unit_inp == "m":
#     number_to_turn = number_to_turn * 1000
#
# if unit_output == "cm":
#     number_to_turn = number_to_turn / 10
# elif unit_output == "m":
#     number_to_turn = number_to_turn / 1000
#
# print(f"{number_to_turn:.3f}")

# 5
# hour = int(input())
# minutes = int(input())
# minutes += 15
#
# hour += minutes // 60
# minutes %= 60
# if hour > 23:
#     hour -= 24
# print(f'{hour}:{minutes:0>2d}')

# 6
# budget = float(input())
# statists = int(input())
# price_for_clothes = float(input())
#
# decor = 0.1 * budget
# price_for_clothes = statists * price_for_clothes
#
# if statists > 150:
#     price_for_clothes -= price_for_clothes * 0.1
#
# needed_money = decor + price_for_clothes
# difference = abs(needed_money - budget)
#
# if needed_money > budget:
#     print("Not enough money!")
#     print(f"Wingard needs {difference:.2f} leva more.")
# else:
#     print("Action!")
#     print(f"Wingard starts filming with {difference:.2f} leva left.")

# 7
# current_record = float(input())
# distance = float(input())
# time_for_1_meter_distance = float(input())
#
# delay = distance // 15 * 12.5
# new_time = distance * time_for_1_meter_distance + delay
#
# if new_time < current_record:
#     print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
# else:
#     difference = new_time - current_record
#     print(f"No, he failed! He was {difference:.2f} seconds slower.")