# 1
# b1 = float(input())
# b2 = float(input())
# h = float(input())
# area = (b1 + b2) * h / 2
# print(f'{area:.2f}')

# 2
# a = float(input())
# h = float(input())
# area = a * h / 2
# print(f'{area:.2f}')

# 3
# celsius = float(input())
# fahrenheit = celsius * 1.8000 + 32.00
# print(f'{fahrenheit:.2f}')

# 4
# vegetables_price_kg = float(input())
# fruits_price_kg = float(input())
# all_kg_vegetables = int(input())
# all_kg_fruits = int(input())
#
# vegetables = all_kg_vegetables * vegetables_price_kg
# fruits = all_kg_fruits * fruits_price_kg
# sum = vegetables + fruits
# sum_in_euro = sum / 1.94
# print(f'{sum_in_euro:.2f}')

# 5
# from math import floor
# height = float(input())
# width = float(input())
#
# width_of_the_hall = width * 100
# corridor = 100
#
# left_space = width_of_the_hall - corridor
# desks_for_row = left_space // 70
#
# height_of_the_hall = height * 100
# rows = height_of_the_hall // 120
#
# number_of_seats = rows * desks_for_row - 3
# print(floor(number_of_seats))

# # 6
# mackerel_price_for_kg = float(input())
# sprat_price_for_kg = float(input())
#
# bonito_kg = float(input())
# horse_mackerel_kg = float(input())
# mussels_kg = float(input())
#
# bonito_price_for_kg = mackerel_price_for_kg + (60/100 * mackerel_price_for_kg)
# horse_mackerel_price_for_kg = sprat_price_for_kg + (80/100 * sprat_price_for_kg)
# mussels_price_for_kg = mussels_kg * 7.50
#
# bonito = bonito_price_for_kg * bonito_kg
# horse_mackerel = horse_mackerel_price_for_kg * horse_mackerel_kg
# mussels = mussels_price_for_kg
#
# sum = bonito + horse_mackerel + mussels
# print(f"{sum:.2f}")

# 7
# steni
# house_height_x = float(input())
# length_side_wall_y = float(input())
# height_triangle_wall_roof_h = float(input())
#
# side_wall_area = house_height_x * length_side_wall_y
# window_area = 1.5 * 1.5
# the_two_side_walls = 2 * side_wall_area - 2 * window_area
# back_wall = house_height_x * house_height_x
# entrance = 1.2 * 2
# entrance_and_back_wall = 2 * back_wall - entrance
# area = the_two_side_walls + entrance_and_back_wall
# green_paint = area / 3.4
#
# # pokriv
# the_two_rectangle_roofs = 2 * (house_height_x * length_side_wall_y)
# the_two_triangle_roofs = 2 * (house_height_x * height_triangle_wall_roof_h / 2)
# area_roof = the_two_rectangle_roofs + the_two_triangle_roofs
# red_paint = area_roof / 4.3
#
# print(f"{green_paint:.2f}")
# print(f"{red_paint:.2f}")

# 8
# import math
# r = float(input())
# calculated_area = math.pi * (r * r)
# calculated_parameter = 2 * math.pi * r
# print(f"{calculated_area:.2f}")
# print(f"{calculated_parameter:.2f}")

# 9
# weather = input()
# if weather == "sunny":
#     print("It's warm outside!")
# elif weather == "cloudy" or "snowy":
#     print("It's cold outside!")

# 10
# degrees = float(input())
# if 26.00 <= degrees <= 35.00:
#     print("Hot")
# elif 20.1 <= degrees <= 25.9:
#     print("Warm")
# elif 15.00 <= degrees <= 20.00:
#     print("Mild")
# elif 12.00 <= degrees <= 14.9:
#     print("Cool")
# elif 5.00 <= degrees <= 11.9:
#     print("Cold")
# else:
#     print("unknown")


