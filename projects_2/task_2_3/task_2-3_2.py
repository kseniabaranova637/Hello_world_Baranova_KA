product = input("Тип продукта (йогурт/кефир): ")
batch_id = input("Номер партии: ")
with open("production_history.txt", "w", encoding="utf-8") as report:
    
    report.write(f"ОТЧЕТ ПРОИЗВОДСТВА\n")
    
    report.write(f"Продукт:\t{product}\n")
    report.write(f"Партия №:\t{batch_id}\n")