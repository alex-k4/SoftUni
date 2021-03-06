# 1
# for number in range(1, 100 + 1):
#     print(number)

# 2
# n = int(input())
# for number in range(1, n+1, 3):
#     print(number)

# 3
# n = int(input())
# for number in range(0, n+1, 2):
#     result = pow(2, number)
#     print(result)

# 4
# n = int(input())
# for number in range(n, 0, -1):
#     print(number)

# 5
# text = input()
# for letter in text:
#     print(letter)

# 6
# text = input()
# sum = 0
# for letter in text:
#     if letter == "a":
#         sum += 1
#     elif letter == "e":
#         sum += 2
#     elif letter == "i":
#         sum += 3
#     elif letter == "o":
#         sum += 4
#     elif letter == "u":
#         sum += 5
#
# print(sum)

# 7
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     numbers = int(input())
#     sum += numbers
#
# print(sum)

# 8
# import sys
# n = int(input())
# max_number = -sys.maxsize
# min_number = sys.maxsize
#
# for num in range(1, n + 1):
#     number = int(input())
#
#     if number > max_number:
#         max_number = number
#     elif number < min_number:
#         min_number = number
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")

# 9
# n = int(input())
# sum_1 = 0
# sum_2 = 0
# for i in range(1, n + 1):
#     number_1 = int(input())
#     sum_1 += number_1
#
# for i in range(1, n + 1):
#     number_2 = int(input())
#     sum_2 += number_2
#
#
#
# if sum_1 == sum_2:
#     print(f"Yes, sum = {sum_1}")
# else:
#     diff = sum_1 - sum_2
#     print(f"No, diff = {abs(diff)}")

# 10
# n = int(input())
# even_position = 0
# odd_position = 0
# for numbers in range(1, n + 1):
#     number = int(input())
#     if numbers % 2 == 0:
#         even_position += number
#     elif numbers % 2 == 1:
#         odd_position += number
#
# if even_position == odd_position:
#     print("Yes")
#     print(f"Sum = {even_position}")
# else:
#     diff = abs(even_position - odd_position)
#     print("No")
#     print(f"Diff = {diff}")



# 11
# age = int(input())
# washing_machine = float(input())
# one_toy_price = int(input())
# toys = 0
# birthday_money = 0
# total_money = 0
# spended_money = 0
#
# # # нечетни рожденни дни --> играчка
# # # четни - пари
# # # За втория рожден ден - 10.00 лв
# # # За всеки следващ четен рд се увеличава с 10.00 лв
# # # В годините в които получава пари, брат и взема по 1.00 лв от тях
# # # Лили продава играчките за П лв и добавя сумата към спестените пари
# # # С парите иска пералня за Х лева
# # # Колко пари е събрала и дали стигат за пералня?
#
# for birthdays in range(1,age + 1):
#     if birthdays % 2 == 1:
#         toys += 1
#     elif birthdays % 2 == 0:
#         birthday_money += 10
#         total_money += birthday_money - 1
#
#
# toys_price = toys * one_toy_price
# total_money += toys_price
#
# if total_money >= washing_machine:
#     left_money = total_money - washing_machine
#     print(f"Yes! {left_money:.2f}")
# elif total_money < washing_machine:
#     needed_money = washing_machine - total_money
#     print(f"No! {needed_money:.2f}")

# 2variant
# age = int(input())
# washing_machine = float(input())
# one_toy_price = int(input())
# toys = 0
# money = 0
# spended_money = 0
#
# for birthdays in range(1,age + 1):
#     if birthdays % 2 == 1:
#         toys += 1
#     elif birthdays % 2 == 0:
#         money = (money + 10)
#         spended_money += money - 1
#
# toys_price = toys * one_toy_price
# all_spended_money = (toys_price + spended_money)
#
# if all_spended_money >= washing_machine:
#     left_money = all_spended_money - washing_machine
#     print(f"Yes! {left_money:.2f}")
# elif all_spended_money < washing_machine:
#     needed_money = washing_machine - all_spended_money
#     print(f"No! {needed_money:.2f}")

# ПРЕРЕШАВАНЕ №1
# 1
# for number in range(1, 100 + 1):
#     print(number)

# 2
# n = int(input())
# for number in range(1, n+1, 3):
#     print(number)

# 3
# n = int(input())
# for number in range(0, n + 1, 2):
#     number = pow(2, number)
#     print(number)

# 4
# n = int(input())
# for number in range(n, 0, -1):
#     print(number)

# 5
# text = input()
# for letter in text:
#     print(letter)

# 6
# text = input()
# sum = 0
# for letter in text:
#     if letter == "a":
#         sum += 1
#     elif letter == "e":
#         sum += 2
#     elif letter == "i":
#         sum += 3
#     elif letter == "o":
#         sum += 4
#     elif letter == "u":
#         sum += 5
#
# print(sum)

# 7
# n = int(input())
# sum = 0
# for number in range(1, n + 1):
#     numbers = int(input())
#     sum += numbers
#
# print(sum)

# 8
# import sys
# n = int(input())
# max_number = -sys.maxsize
# min_number = sys.maxsize
#
# for num in range(1, n + 1):
#     number = int(input())
#
#     if number > max_number:
#         max_number = number
#     elif number < min_number:
#         min_number = number
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")

# 9
# n = int(input())
# left_sum = 0
# odd_sum = 0
# for number in range(1, n + 1):
#     numbers = int(input())
#     left_sum += numbers
#
# for number in range(1, n + 1):
#     numbers = int(input())
#     odd_sum += numbers
#
# if left_sum == odd_sum:
#     print(f"Yes, sum = {left_sum}")
# elif left_sum != odd_sum:
#     diff = abs(left_sum - odd_sum)
#     print(f"No, diff = {diff}")

# 10
# n = int(input())
# even_sum = 0
# odd_sum = 0
#
# for number in range(1, n + 1):
#     numbers = int(input())
#     if number % 2 == 0:
#         even_sum += numbers
#     elif number % 2 == 1:
#         odd_sum += numbers
#
# if even_sum == odd_sum:
#     print(f"Yes")
#     print(f"Sum = {even_sum}")
# elif even_sum != odd_sum:
#     diff = abs(even_sum - odd_sum)
#     print(f"No")
#     print(f"Diff = {diff}")

# 11
# age = int(input())
# washing_machine_price = float(input())
# one_toy_price = int(input())
# toys = 0
# birthday_money = 0
# total_money = 0
#
# for birthday in range(1, age + 1):
#     if birthday % 2 == 1:
#         toys += 1
#     elif birthday % 2 == 0:
#         birthday_money += 10
#         total_money += birthday_money - 1
#
# toys_price = toys * one_toy_price
# total_money += toys_price
#
# if total_money >= washing_machine_price:
#     left_money = total_money - washing_machine_price
#     print(f"Yes! {left_money:.2f}")
# elif total_money < washing_machine_price:
#     diff = washing_machine_price - total_money
#     print(f"No! {diff:.2f}")

# ПРЕРЕШАВАНЕ 2
# 1
# for number in range(1, 100 + 1):
#     print(number)

# 2
# n = int(input())
# for number in range(1, n + 1, 3):
#     print(number)

# 3
# n = int(input())
# for number in range(0, n+1, 2):
#     number = pow(2,number)
#     print(number)

# 4
# n = int(input())
# for number in range(n, 0, -1):
#     print(number)

# 5
# text = input()
# for letter in text:
#     print(letter)

# 6
# text = input()
# sum = 0
# for letter in text:
#     if letter == "a":
#         sum += 1
#     elif letter == "e":
#         sum += 2
#     elif letter == "i":
#         sum += 3
#     elif letter == "o":
#         sum += 4
#     elif letter == "u":
#         sum += 5
#
# print(sum)

# 7
# n = int(input())
# sum = 0
# for number in range(1, n + 1):
#     numbers = int(input())
#     sum += numbers
#
# print(sum)

# 8
# import sys
# n = int(input())
# max_number = -sys.maxsize
# min_number = sys.maxsize
# for number in range(1, n + 1):
#     numbers = int(input())
#     if numbers > max_number:
#         max_number = numbers
#     elif numbers < min_number:
#         min_number = numbers
#
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")

# 9
# n = int(input())
# left_sum = 0
# right_sum = 0
# for number in range(1, n+1):
#     numbers = int(input())
#     left_sum += numbers
#
# for number in range(1, n+1):
#     numbers = int(input())
#     right_sum += numbers
#
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(left_sum - right_sum)
#     print(f"No, diff = {diff}")

# 10
# n = int(input())
# even_position = 0
# odd_position = 0
# for number in range(1, n + 1):
#     numbers = int(input())
#     if number % 2 == 0:
#         even_position += numbers
#     elif number % 2 == 1:
#         odd_position += numbers
#
# if even_position == odd_position:
#     print("Yes")
#     print(f"Sum = {even_position}")
# else:
#     diff = abs(even_position - odd_position)
#     print(f"No")
#     print(f"Diff = {diff}")

# 11
# age = int(input())
# washing_machine_price = float(input())
# one_toy_price = int(input())
# toys = 0
# birthday_money = 0
# total_money = 0
# for birthday in range(1, age+1):
#     if birthday % 2 == 1:
#         toys += 1
#     elif birthday % 2 == 0:
#         birthday_money += 10
#         total_money += birthday_money - 1
# toys_price = toys * one_toy_price
# total_money += toys_price
#
# if total_money >= washing_machine_price:
#     left_money = total_money - washing_machine_price
#     print(f"Yes! {left_money:.2f}")
# elif total_money < washing_machine_price:
#     needed_money = washing_machine_price - total_money
#     print(f"No! {needed_money:.2f}")

# 12312321
# age = int(input())
# washing_machine = float(input())
# toy_price = int(input())
# toys_count = 0
# lily_money = 0
# birthday_money=0;
#
#
# for birthdays in range(age):
#     if birthdays % 2 == 0:
#         lily_money += 9
#         birthday_money += lily_money
#     else:
#         toys_count += 1
#
# toys_price = toys_count * toy_price
# saved_money = (toys_price + birthday_money)
#
# if saved_money >= washing_machine:
#     left_money = saved_money - washing_machine
#     print(f"Yes! {left_money:.2f}")
# else:
#     needed_money = washing_machine - saved_money
#     print(f"No! {needed_money:.2f}")

