N = int(input("Введите N: "))
if N <= 0:
    print("Ошибка, N > 0")
else:
    sum = 0
    i = 1
    while i <= N:
        x = int(input("Введите число: "))
        if i % 2 != 0:
            sum += x
        i += 1
    print(sum)