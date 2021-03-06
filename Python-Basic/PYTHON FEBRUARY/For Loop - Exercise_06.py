# 1
# type_projection = input()
# rows = int(input())
# columns = int(input())
#
# income = 0
# cinema_capacity = rows * columns
#
# if type_projection == "Premiere":
#     income = cinema_capacity * 12.00
# elif type_projection == "Normal":
#     income = cinema_capacity * 7.50
# elif type_projection == "Discount":
#     income = cinema_capacity * 5.00
#
# print(f"{income:.2f} leva")

# 2
# degrees = int(input())
# time_of_day = input()
# outfit = ""
# shoes = ""
#
# if time_of_day == "Morning":
#     if 10 <= degrees <= 18:
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif 18 < degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
# elif time_of_day == "Afternoon":
#     if 10 <= degrees <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < degrees <= 24:
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif degrees >= 25:
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
# elif time_of_day == "Evening":
#     if 10 <= degrees <= 18:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif 18 < degrees <= 24:
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif degrees >= 25:
#         outfit = "Shirt"
#         shoes = "Moccasins"
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# 3 greshen e
# type_of_flowers = input()
# number_of_flowers = int(input())
# budget = int(input())
# price = 0
#
# rose_price = 5 * number_of_flowers
# dahlia_price = 3.80 * number_of_flowers
# tulip_price = 2.80 * number_of_flowers
# narcissus_price = 3 * number_of_flowers
# gladiolus_price = 2.50 * number_of_flowers
#
# if type_of_flowers == "Roses":
#     if number_of_flowers > 80:
#         rose_price = rose_price - 0.1 * rose_price
#         price = rose_price
# elif type_of_flowers == "Dahlias":
#     if number_of_flowers > 90:
#         dahlia_price = dahlia_price - 0.15 * dahlia_price
#         price = dahlia_price
# elif type_of_flowers == "Tulips":
#     if number_of_flowers > 80:
#         tulip_price = tulip_price - 0.15 * tulip_price
#         price = tulip_price
# elif type_of_flowers == "Narcissus":
#     if number_of_flowers < 120:
#         narcissus_price = narcissus_price + 0.15 * narcissus_price
#         price = narcissus_price
# elif type_of_flowers == "Gladiolus":
#     if number_of_flowers < 80:
#         gladiolus_price = gladiolus_price + 0.20 * gladiolus_price
#         price = gladiolus_price
#
# if budget >= price:
#     left_sum = abs(budget - price)
#     print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {left_sum:.2f} leva left.")
# elif budget < price:
#     needed_sum = abs(price - budget)
#     print(f"Not enough money, you need {needed_sum:.2f} leva more.")












