N = int(input("Введите N: "))
if N <= 0:
    print("Ошибка, N > 0")
else:
    sum = 0
    count = 0
    i = 1
    while i <= N:
        x = float(input("введите число: "))
        if i % 2 == 0: 
            sum += x
            count += 1
        i += 1
    if count > 0:
        avg = sum / count
        print(avg)