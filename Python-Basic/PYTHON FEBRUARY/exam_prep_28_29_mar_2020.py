# 1
# number_bitcoins = int(input())
# number_chinese_yuan = float(input())
# commission = float(input())
#
# bitcoins_bgn = number_bitcoins * 1168
# yuan_euro = number_chinese_yuan * 0.15
# yuan_in_bgn = yuan_euro * 1.76
# sum_euro = (bitcoins_bgn + yuan_in_bgn) / 1.95
# commission_new = commission / 100 * sum_euro
# result = sum_euro - commission_new
# print(f"{result:.2f}")

# 2
# min_per_walk = int(input())
# walks_per_day = int(input())
# calls_eaten = int(input())
#
# total_minutes = min_per_walk * walks_per_day
# burnt_calls = total_minutes * 5
#
# if burnt_calls >= (calls_eaten/2):
#     print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calls}.")
# else:
#     print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calls}.")

# # 3
# sum_we_have = float(input())
# gender = input()
# age = int(input())
# sport = input()
# price = 0
#
# if gender == "m":
#     if sport == "Gym":
#         price = 42
#     elif sport == "Boxing":
#         price = 41
#     elif sport == "Yoga":
#         price = 45
#     elif sport == "Zumba":
#         price = 34
#     elif sport == "Dances":
#         price = 51
#     elif sport == "Pilates":
#         price = 39
# elif gender == "f":
#     if sport == "Gym":
#         price = 35
#     elif sport == "Boxing":
#         price = 37
#     elif sport == "Yoga":
#         price = 42
#     elif sport == "Zumba":
#         price = 31
#     elif sport == "Dances":
#         price = 53
#     elif sport == "Pilates":
#         price = 37
#
# if age <= 19:
#     price = price - 0.2 * price
#
# if sum_we_have >= price:
#     print(f"You purchased a 1 month pass for {sport}.")
# elif sum_we_have < price:
#     needed_money = price - sum_we_have
#     print(f"You don't have enough money! You need ${needed_money:.2f} more.")


# sport = ('Gym', 'Boxing', 'Yoga', 'Zumba', 'Dances', 'Pilates')
# man = (42, 41, 45, 34, 51, 39)
# woman = (35, 37, 42, 31, 53, 37)
# budget, sex, years_old, sport_i = float(input()), input(), int(input()), input()
#
# sum = 0;
#
# for i in range(len(sport)):
#     if sport_i == sport[i]:
#         if years_old > 19:
#             if sex == "m":
#                 sum = man[i]
#             elif sex == "f":
#                 sum = woman[i]
#         else:
#             if sex == "m":
#                 sum = man[i] - man[i] * 20/100
#             elif sex == "f":
#                 sum = woman[i] - woman[i] * 20/100
#
# if budget >= sum:
#     print(f"You purchased a 1 month pass for {sport_i}.")
# else:
#     print(f"You don't have enough money! You need ${sum - budget:.2f} more.")

# 4
# days = int(input()) # 3
# all_food = float(input())
# total_eaten_food = 0
#
# for day in range(days):
#     eaten_food_dog = int(input())
#     eaten_food_cat = int(input())
#     total_eaten_food += eaten_food_cat + eaten_food_dog
#
#     if day % 3 == 0:
#         biscuits = 10/100 * (eaten_food_dog + eaten_food_cat)
# percentage_eaten_food = total_eaten_food * all_food
# percentage_eaten_food_dog = eaten_food_dog * total_eaten_food
# percentage_eaten_food_cat =








