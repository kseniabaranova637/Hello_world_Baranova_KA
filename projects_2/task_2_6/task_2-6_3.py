donor = input("Введите группe крови донора (I, II, III, IV): ").strip().upper()
patient = input("Введите группe крови пациента (I, II, III, IV): ").strip().upper()
if donor == "I" or donor == patient:
    print("Переливание возможно")
else:
    print("Переливание невозможно")