fio = input("ФИО пациента: ")
symptoms = input("Основные жалобы: ")

with open("patient_card.txt", "w", encoding="utf-8") as card:
    
    card.write(f"{fio}\t| Жалоба: {symptoms}\n")