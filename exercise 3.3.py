""""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""
result = 0
def my_func(num1, num2, num3):
    num_list = [num1, num2, num3]
    result = sum(num_list) - min(num1, num2, num3)
    return result

print(my_func(8, 7, 9))