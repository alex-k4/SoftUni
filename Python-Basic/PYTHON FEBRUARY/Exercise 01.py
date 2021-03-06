# 1
# airline = input()
# tickets_for_adults = int(input())
# tickets_for_kids = int(input())
# price_tickets_for_adults = float(input())
# price_services_fee = float(input())
#
# price_tickets_for_kids = price_tickets_for_adults - 0.7 * price_tickets_for_adults
# price_for_adults_with_price_services_fee = price_tickets_for_adults + price_services_fee
# price_for_kids_with_price_services_fee = price_tickets_for_kids + price_services_fee
#
# sum = (tickets_for_kids * price_for_kids_with_price_services_fee) \
#     + (tickets_for_adults * price_for_adults_with_price_services_fee)
#
# final_sum = 0.2 * sum
# print(f"The profit of your agency from {airline} tickets is {final_sum:.2f} lv.")

# 2
# price = 0
#
# price_luggage_over_20_kg = float(input())
# kg_luggage = float(input())
# days_to_travel = int(input())
# number_of_luggage = int(input())
#
# if kg_luggage <= 10:
#     price = 0.2 * price_luggage_over_20_kg
# elif 10 < kg_luggage <= 20:
#     price = 0.5 * price_luggage_over_20_kg
# elif kg_luggage > 20:
#     price = price_luggage_over_20_kg
#
# if days_to_travel > 30:
#     price = price + 0.1 * price
# elif 7 <= days_to_travel <= 30:
#     price = price + 0.15 * price
# elif days_to_travel < 7:
#     price = price + 0.4 * price
#
# sum = number_of_luggage * price
# print(f"The total price of bags is: {sum:.2f} lv.")

# 3
# price = 0
#
# number_of_joinery = int(input())
# type_of_joinery = input()
# shipment_method = input()
#
# if number_of_joinery < 10:
#     print("Invalid order")
#     exit(0)
#
# if type_of_joinery == "90X130":
#     price = 110 * number_of_joinery
#     if number_of_joinery > 60:
#         price = price - price * 8 / 100
#     elif 30 < number_of_joinery <= 60:
#         price = price - price * 5 / 100
#
# elif type_of_joinery == "100X150":
#     price = 140 * number_of_joinery
#     if number_of_joinery > 80:
#         price = price - price * 10/100
#     elif 40 < number_of_joinery <= 80:
#         price = price - price * 6/100
#
# elif type_of_joinery == "130X180":
#     price = 190 * number_of_joinery
#     if number_of_joinery > 50:
#         price = price - price * 12/100
#     elif 20 < number_of_joinery <= 50:
#         price = price - price * 7/100
#
# elif type_of_joinery == "200X300":
#     price = 250 * number_of_joinery
#     if number_of_joinery > 50:
#         price = price - price * 14/100 # price = 100 *1.4 = 140
#     elif 25 < number_of_joinery <= 50:
#         price = price - price * 9/100
#
#
# if shipment_method == "With delivery":
#     price += 60
#
# if number_of_joinery > 99:
#     price = price - price * 4/100
#
# print(f"{price:.2f} BGN")

# 4
# n = int(input())
# total_points = 0
# red_balls = 0
# orange_balls = 0
# yellow_balls = 0
# white_balls = 0
# other_colours_count = 0
# black_balls_count = 0
#
# for x in range(n):
#     color = input()
#
#     if color == "red":
#         red_balls += 1
#         total_points += 5
#     elif color == "orange":
#         orange_balls += 1
#         total_points += 10
#     elif color == "yellow":
#         yellow_balls += 1
#         total_points += 15
#     elif color == "white":
#         white_balls += 1
#         total_points += 20
#     elif color == "black":
#         total_points /= 2
#         black_balls_count += 1
#     else:
#         other_colours_count += 1
#
# print(f"Total points: {int(total_points)}")
# print(f"Points from red balls: {red_balls}")
# print(f"Points from orange balls: {orange_balls}")
# print(f"Points from yellow balls: {yellow_balls}")
# print(f"Points from white balls: {white_balls}")
# print(f"Other colors picked: {other_colours_count}")
# print(f"Divides from black balls: {black_balls_count}")

# 5
# name = input()
# number_of_goals = int(input())

# for x in range(5):
#     print(x)

# data = input()
# best_player_name = ""
# best_player_goals = 0
#
# while data != "END":
#     player_name = data
#     player_goals = int(input())
#     # --------
#
#
#     if player_goals > best_player_goals:
#         best_player_name = player_name
#         best_player_goals = player_goals
#
#     if player_goals >= 10:
#         break
#
#     data = input()
# print(f"{best_player_name} is the best player!")
#
# if best_player_goals >= 3:
#     print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
# else:
#     print(f"He has scored {best_player_goals} goals.")











