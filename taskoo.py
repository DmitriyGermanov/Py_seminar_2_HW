# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

number_of_coins = int(input("Введите количество монет: "))
if (number_of_coins == 1):
    print("На столе лежит одна монета")
elif (number_of_coins == 0):
    print("На столе не лежит ни одной монеты")
else:
    count = 1
    coin_heads = 0
    coin_tails = 0
    for i in range(number_of_coins):
        coin_location = 3
        while (coin_location < -1 or coin_location > 1):
            coin_location = int(
                input(f"Введите положение монеты {count} (0 - решка, 1 - орел): "))
            if (coin_location != 0 and coin_location != 1):
                print("Введите корректное положение монеты")
            else:
                count += 1
        if (coin_location == 1):
            coin_heads += 1
        else:
            coin_tails += 1
    if (coin_heads == 0 or coin_tails == 0):
        print("Все монеты лежат на одной стороне")
    elif (coin_heads < coin_tails):
        print(
            f"Минимальное количество монет, которые нужно перевернуть = {coin_heads}")
    else:
        print(
            f"Минимальное количество монет, которые нужно перевернуть = {coin_tails}")
