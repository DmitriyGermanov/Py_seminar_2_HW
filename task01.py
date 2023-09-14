# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Введите сумму чисел: "))
if (sum == 0):
    print("Искомые числа 0 и 0")
else:
    multiply = int(input("Введите произведение чисел: "))
    if (sum - multiply == 1):
        print(f"Первое число = {multiply}, второе число = {1}")
    if (multiply == 0):
        print(f"Первое число = {0}, второе число = {sum}")
    else:
        flag = True
        first_number = 0
        second_number = 0
        count = 1
        while (flag):
            if (multiply % count == 0 and ((sum - count) * count) == multiply):
                flag = False
                first_number = count
                second_number = sum - count
            if (count == multiply):
                flag = False
            else:
                count += 1
        print(f"Первое число = {first_number}, второе число = {second_number}")
