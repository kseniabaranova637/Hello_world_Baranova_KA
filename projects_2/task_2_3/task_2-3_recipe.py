name_sreda = input("Введите название питательной среды:")
processed_name = name_sreda.upper()
con_agara = input("Введите концентрацию агара(%):")
temper = input("Введите температуру стерилизации:")
with open("recipe.txt", "w", encoding="utf-8") as recept:
    recept.write(f"{processed_name}\n")
    recept.write(f"Концентрация агара (%): {con_agara}\n")
    recept.write(f"Температура стерелизации: {temper}\n")
    recept.write("Файл 'recipe.txt' успешно сформирован!")