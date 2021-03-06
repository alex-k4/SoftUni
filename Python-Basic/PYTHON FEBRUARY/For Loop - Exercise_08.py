# 1
# for number in range(1, 1000 +1):
#     if number % 10 == 7:
#         print(number)

# 2
# import sys
# n = int(input())
# max_number = -sys.maxsize
# sum_of_all = 0
#
# for number in range(n):
#     current_number = int(input())
#     if current_number > max_number:
#         max_number = current_number
#     sum_of_all += current_number
# if max_number == sum_of_all - max_number:
#     print("Yes")
#     print(f"Sum = {max_number}")
# else:
#     diff = abs(max_number-(sum_of_all - max_number))
#     print(f"No")
#     print(f"Diff = {diff}")

# 3
# import sys
# n = int(input())
# odd_sum = 0
# odd_min_number = sys.maxsize
# odd_max_number = -sys.maxsize
# even_sum = 0
# even_min_number = sys.maxsize
# even_max_number = -sys.maxsize
#
# for position in range(1, n + 1):
#     numbers = float(input())
#     if position % 2 == 0:
#         even_sum += numbers
#         if numbers < even_min_number:
#             even_min_number = numbers
#         if numbers > even_max_number:
#             even_max_number = numbers
#     else:
#         odd_sum += numbers
#         if numbers < odd_min_number:
#             odd_min_number = numbers
#         if numbers > odd_max_number:
#             odd_max_number = numbers
#
#
# print(f"OddSum={odd_sum:.2f},")
# if odd_min_number == sys.maxsize:
#     print(f"OddMin=No,")
# else:
#     print(f"OddMin={odd_min_number:.2f},")
# if odd_max_number == - sys.maxsize:
#     print(f"OddMax=No,")
# else:
#     print(f"OddMax={odd_max_number:.2f},")
#
# print(f"EvenSum={even_sum:.2f},")
# if even_min_number == sys.maxsize:
#     print(f"EvenMin=No,")
# else:
#     print(f"EvenMin={even_min_number:.2f},")
# if even_max_number == - sys.maxsize:
#     print(f"EvenMax=No")
# else:
#     print(f"EvenMax={even_max_number:.2f}")

# 4
# n = int(input())
# numbers_count = 0
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
#
# for numbers in range(n):
#     current_number = int(input())
#     if current_number < 200:
#         p1 += 1
#     elif 200 <= current_number <= 399:
#         p2 += 1
#     elif 400 <= current_number <= 599:
#         p3 += 1
#     elif 600 <= current_number <= 799:
#         p4 += 1
#     elif current_number >= 800:
#         p5 += 1
#
# print(f"{p1 / n * 100:.2f}%")
# print(f"{p2 / n * 100:.2f}%")
# print(f"{p3 / n * 100:.2f}%")
# print(f"{p4 / n * 100:.2f}%")
# print(f"{p5 / n * 100:.2f}%")

# 5
# n = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
#
# for numbers in range(n):
#     current_number = int(input())
#     if current_number % 2 == 0:
#         p1 += 1
#     if current_number % 3 == 0:
#         p2 += 1
#     if current_number % 4 == 0:
#         p3 += 1
#
# print(f"{(p1 / n * 100):.2f}%")
# print(f"{(p2 / n * 100):.2f}%")
# print(f"{(p3 / n * 100):.2f}%")

# 6
# number_opened_tabs = int(input())
# salary = int(input())
# still_have_salary = True
# for opened_tab in range(number_opened_tabs):
#     current_tab = input()
#     if current_tab == "Facebook":
#         salary -= 150
#     elif current_tab == "Instagram":
#         salary -= 100
#     elif current_tab == "Reddit":
#         salary -= 50
#     if salary <= 0:
#         still_have_salary = False
#
# if still_have_salary:
#     print(salary)
# else:
#     print("You have lost your salary.")

# Пререшаване
# 1
# for number in range(1, 1000 + 1):
#     if number % 10 == 7:
#         print(number)

# 2
# import sys
# n = int(input())
# sum_of_all = 0
# max_number = - sys.maxsize
# min_number = sys.maxsize
# for number in range(1, n + 1):
#     current_number = int(input())
#     if current_number > max_number:
#         max_number = current_number
#     sum_of_all += current_number
# if max_number == sum_of_all - max_number:
#     print("Yes")
#     print(f"Sum = {max_number}")
# else:
#     diff = abs(max_number - (sum_of_all - max_number))
#     print("No")
#     print(f"Diff = {diff}")

# 3
# import sys
# count_of_numbers = int(input())
# even_sum = 0
# even_min_number = sys.maxsize
# even_max_number = - sys.maxsize
# odd_sum = 0
# odd_min_number = sys.maxsize
# odd_max_number = - sys.maxsize
#
# for numbers in range(1, count_of_numbers + 1):
#     current_number = float(input())
#     if numbers % 2 == 0:
#         even_sum += current_number
#         if current_number > even_max_number:
#             even_max_number = current_number
#         if current_number < even_min_number:
#             even_min_number = current_number
#     else:
#         odd_sum += current_number
#         if current_number > odd_max_number:
#             odd_max_number = current_number
#         if current_number < odd_min_number:
#             odd_min_number = current_number
#
# print(f"OddSum={odd_sum:.2f},")
# if odd_min_number == sys.maxsize:
#     print(f"OddMin=No,")
# else:
#     print(f"OddMin={odd_min_number:.2f},")
# if odd_max_number == - sys.maxsize:
#     print(f"OddMax=No,")
# else:
#     print(f"OddMax={odd_max_number:.2f},")
#
# print(f"EvenSum={even_sum:.2f},")
# if even_min_number == sys.maxsize:
#     print(f"EvenMin=No,")
# else:
#     print(f"EvenMin={even_min_number:.2f},")
# if even_max_number == - sys.maxsize:
#     print(f"EvenMax=No")
# else:
#     print(f"EvenMax={even_max_number:.2f}")

# 4
# n = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
# for numbers in range(n):
#     current_number = int(input())
#     if current_number < 200:
#         p1 += 1
#     if 200 <= current_number <= 399:
#         p2 += 1
#     if 400 <= current_number <= 599:
#         p3 += 1
#     if 600 <= current_number <= 799:
#         p4 += 1
#     if current_number >= 800:
#         p5 += 1
#
# print(f"{p1 / n * 100:.2f}%")
# print(f"{p2 / n * 100:.2f}%")
# print(f"{p3 / n * 100:.2f}%")
# print(f"{p4 / n * 100:.2f}%")
# print(f"{p5 / n * 100:.2f}%")

# 5
# n = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
# for numbers in range(n):
#     current_number = int(input())
#     if current_number % 2 == 0:
#         p1 += 1
#     if current_number % 3 == 0:
#         p2 += 1
#     if current_number % 4 == 0:
#         p3 += 1
#
# print(f"{p1/n * 100:.2f}%")
# print(f"{p2/n * 100:.2f}%")
# print(f"{p3/n * 100:.2f}%")

# 6
# opened_tabs = int(input())
# salary = int(input())
# still_have_salary = True
# for tabs in range(opened_tabs):
#     current_tabs = input()
#     if current_tabs == "Facebook":
#         salary -= 150
#     if current_tabs == "Instagram":
#         salary -= 100
#     if current_tabs == "Reddit":
#         salary -= 50
#     if salary <= 0:
#         still_have_salary = False
#
# if still_have_salary:
#     print(salary)
# else:
#     print(f"You have lost your salary.")
















