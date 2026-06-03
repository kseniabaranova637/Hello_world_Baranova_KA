N = int(input("Введите N: "))
if N <= 0:
    print("Ошибка, N должно быть > 0")
else:
    max = float(input("Введите число: "))
    i = 2
    while i <= N:
        x = float(input("Введите число: "))
        if x > max:
            max = x
        i = i + 1
    print(max)