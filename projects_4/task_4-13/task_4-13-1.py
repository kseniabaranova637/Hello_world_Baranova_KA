A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
D = float(input("Введите D: "))
min = A
if B < min:
    min = B
if C < min:
    min = C
if D < min:
    min = D
print(f"min = {min:.0f}" if min.is_integer() else f"min = {min}")