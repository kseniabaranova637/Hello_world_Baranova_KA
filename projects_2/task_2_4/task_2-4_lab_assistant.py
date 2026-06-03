volume_pastv = int(input("Введите необходимый объём раствора "))
massa_sol = volume_pastv * 0.009 
volume_water = volume_pastv
with open("recipe.txt", "w", encoding="utf-8") as recept:
    recept.write("Отчёт по приготовлению:\n")
    recept.write("-----------------------\n")
    recept.write(f"Общий объём: {volume_pastv} мл\n")
    recept.write(f"Масса соли: {massa_sol} г\n")
    recept.write(f"Объём воды: {volume_water} мл\n")