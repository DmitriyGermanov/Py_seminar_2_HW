# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N: "))

degree_result = 1
print(f"Степени двойки до N: {degree_result}", end=" ")
degree_result = 2
while (degree_result <= N):
    print(degree_result, end=" ")
    degree_result = degree_result * 2
