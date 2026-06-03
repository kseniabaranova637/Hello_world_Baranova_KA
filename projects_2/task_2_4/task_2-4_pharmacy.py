capsyl = int(input("Введите общее количество произведенных капсул: "))
upac = int(input("Введите вместимость одной упаковки(шт): "))
poln_up = capsyl // upac
caps_ost = capsyl % upac
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {poln_up}")
print(f"Остаток капсул: {caps_ost}")