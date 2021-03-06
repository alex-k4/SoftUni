# # 12
# town = input()
# sales = float(input())
# commission = 0
#
# if town == "Sofia":
#     if 0 <= sales <= 500:
#         commission = 5/100 * sales
#     elif 500 < sales <= 1000:
#         commission = 7/100 * sales
#     elif 1000 < sales <= 10000:
#         commission = 8/100 * sales
#     elif sales > 10000:
#         commission = 12/100 * sales
#     else:
#         print("error")
#         exit(0)
# elif town == "Varna":
#     if 0 <= sales <= 500:
#         commission = 4.5/100 * sales
#     elif 500 < sales <= 1000:
#         commission = 7.5/100 * sales
#     elif 1000 < sales <= 10000:
#         commission = 10/100 * sales
#     elif sales > 10000:
#         commission = 13/100 * sales
#     else:
#         print("error")
#         exit(0)
# elif town == "Plovdiv":
#     if 0 <= sales <= 500:
#         commission = 5.5/100 * sales
#     elif 500 < sales <= 1000:
#         commission = 8/100 * sales
#     elif 1000 < sales <= 10000:
#         commission = 12/100 * sales
#     elif sales > 10000:
#         commission = 14.5/100 * sales
#     else:
#         print("error")
#         exit(0)
# elif town != "Sofia" or town != "Varna" or town != "Plovdiv":
#     print("error")
#     exit(0)
# elif sales < 0:
#     print("error")
#     exit(0)
#
# print(f"{commission:.2f}")


# # 1
# number = int(input())
# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# elif number == 7:
#     print("Sunday")
# else:
#     print("Error")

# # 2
# day = input()
# if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
#     print("Working day")
# elif day == "Saturday" or day == "Sunday":
#     print("Weekend")
# else:
#     print("Error")

# 3
# animal = input()
# if animal == "dog":
#     print("mammal")
# elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
#     print("reptile")
# else:
#     print("unknown")

# 4
# age = float(input())
# sex = input()
# if sex == "m":
#     if age >= 16:
#         print("Mr.")
#     elif age < 16:
#         print("Master")
# elif sex == "f":
#     if age >= 16:
#         print("Ms.")
#     elif age < 16:
#         print("Miss")

# 5
# product = input()
# town = input()
# quantity = float(input())
# price = 0
# if town == "Sofia":
#     if product == "coffee":
#         price = quantity * 0.50
#     elif product == "water":
#         price = quantity * 0.80
#     elif product == "beer":
#         price = quantity * 1.20
#     elif product == "sweets":
#         price = quantity * 1.45
#     elif product == "peanuts":
#         price = quantity * 1.60
# if town == "Plovdiv":
#     if product == "coffee":
#         price = quantity * 0.40
#     elif product == "water":
#         price = quantity * 0.70
#     elif product == "beer":
#         price = quantity * 1.15
#     elif product == "sweets":
#         price = quantity * 1.30
#     elif product == "peanuts":
#         price = quantity * 1.50
# if town == "Varna":
#     if product == "coffee":
#         price = quantity * 0.45
#     elif product == "water":
#         price = quantity * 0.70
#     elif product == "beer":
#         price = quantity * 1.10
#     elif product == "sweets":
#         price = quantity * 1.35
#     elif product == "peanuts":
#         price = quantity * 1.55
# print(price)

# 6
# number = float(input())
# if -100 <= number <= 100 and number !=0:
#     print("Yes")
# else:
#     print("No")

# 7
# hour = int(input())
# day = input()
# if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
#     if 10 <= hour <= 18:
#         print("open")
#     else:
#         print("closed")
# else:
#     print("closed")

# 8
# day = input()
# price = 0
# if day == "Monday" or day == "Tuesday":
#     price = 12
# elif day == "Wednesday" or day == "Thursday":
#     price = 14
# elif day == "Friday":
#     price = 12
# elif day == "Saturday" or day == "Sunday":
#     price = 16
# print(price)

# 9
# product = input()
# if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
#     print("fruit")
# elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
#     print("vegetable")
# else:
#     print("unknown")

# 10
# number = int(input())
# if 100 <= number <= 200 or number == 0:
#     pass
# else:
#     print("invalid")

# 11
# fruit = input()
# day = input()
# quantity = float(input())
# price = 0
# if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
#     if fruit == "banana":
#         price = 2.50 * quantity
#     elif fruit == "apple":
#         price = 1.20 * quantity
#     elif fruit == "orange":
#         price = 0.85 * quantity
#     elif fruit == "grapefruit":
#         price = 1.45 * quantity
#     elif fruit == "kiwi":
#         price = 2.70 * quantity
#     elif fruit == "pineapple":
#         price = 5.50 * quantity
#     elif fruit == "grapes":
#         price = 3.85 * quantity
#     else:
#         print("error")
#         exit(0)
# elif day == "Saturday" or day == "Sunday":
#     if fruit == "banana":
#         price = 2.70 * quantity
#     elif fruit == "apple":
#         price = 1.25 * quantity
#     elif fruit == "orange":
#         price = 0.90 * quantity
#     elif fruit == "grapefruit":
#         price = 1.60 * quantity
#     elif fruit == "kiwi":
#         price = 3.00 * quantity
#     elif fruit == "pineapple":
#         price = 5.60 * quantity
#     elif fruit == "grapes":
#         price = 4.20 * quantity
#     else:
#         print("error")
#         exit(0)
# else:
#     print("error")
#     exit(0)
# print(f"{price:.2f}")

# 13
# days = int(input())
# type_room = input()
# rate = input()
# discount = 0
# price = 0
#
# if type_room == "room for one person":
#     if days - 1 < 10:
#         discount = (days - 1) * 18.00
#     elif 10 <= days - 1 <= 15:
#         discount = (days - 1) * 18.00
#     elif days - 1 > 15:
#         discount = (days - 1) * 18.00
#
# elif type_room == "apartment":
#     if days - 1 < 10:
#         price = (days - 1) * 25.00
#         discount = price - price * 30 / 100
#     elif 10 <= days - 1 <= 15:
#         price = (days - 1) * 25.00
#         discount = price - price * 35 / 100
#     elif days - 1 > 15:
#         price = (days - 1) * 25.00
#         discount = price - price * 50 / 100
#
# elif type_room == "president apartment":
#     if days - 1 < 10:
#         price = (days - 1) * 35.00
#         discount = price - price * 10 / 100
#     elif 10 <= days - 1 <= 15:
#         price = (days - 1) * 35.00
#         discount = price - price * 15 / 100
#     elif days - 1 > 15:
#         price = (days - 1) * 35.00
#         discount = price - price * 20 / 100
#
# if rate == "positive":
#     discount += 25 / 100 * discount
# elif rate == "negative":
#     discount -= 10 / 100 * discount
#
# print(f"{discount:.2f}")


