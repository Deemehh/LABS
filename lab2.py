##### ЗАДАНИЕ 1
def greet(name):
    print(f"добрый день, {name}")
erm = input("введите ваше имя: ")
greet(erm)

##### ЗАДАНИЕ 2
# def square(num):
#     return num ** 2
#
# erm = int(input("введите число: "))
# result = square(erm)
# print(f"квадрат {erm} = {result}")
#
##### ЗАДАНИЕ 3
# def max_of_two(x, y):
#     return max(x, y)
#
# erm1 = int(input("введите первое число: "))
# erm2 = int(input("введите второе число: "))
#
# result = max_of_two(erm1, erm2)
# print(f"наибольшее число: {result}")
#
##### ЗАДАНИЕ 4
# def describe_person(name, age=30):
#     print(f"Имя: {name}, Возраст: {age}")
#
# describe_person("Forsen", 33)
# describe_person("Denis", 19)
# describe_person("David")
#
##### ЗАДАНИЕ 5
# def is_prime(num):
#   num = abs(num)
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# erm = int(input("введите число: "))
# if is_prime(erm):
#     print(f"число {erm} является простым")
# else:
#     print(f"число {erm} является составным")
