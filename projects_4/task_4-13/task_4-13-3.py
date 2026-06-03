N = int(input("Введите N: "))
if N < 0:
    print("Ошибка, N > 0")
else:
    f = 1
    i = 1
    while i <= N:
        f = f * i
        i = i + 1
    print(f)