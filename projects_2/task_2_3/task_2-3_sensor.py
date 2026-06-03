operator_name = input("Введите имя оператора:")
davlenie = input("Введите текущее значение датчика давления:")
with open("sensor_log.txt", "w", encoding="utf-8") as logo:
    logo.write(f"Оператор:\t{operator_name}\n")
    logo.write(f"Давление (Па):\t{davlenie}\n")
    logo.write(f"Данные успешно сохранены в sensor_log.txt")