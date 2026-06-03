import psycopg2

try:
    # 1. Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres_task",
        password="student",
        database="student"
    )
    
    # Создаем курсор для выполнения команд
    cursor = connection.cursor()

    # 2. Выполняем SQL-запрос (объединяем таблицы по id и product_id)
    query = """
    SELECT 
        p.name, 
        pr.price 
    FROM products AS p
    JOIN prices AS pr ON p.id = pr.product_id;
    """
    cursor.execute(query)

    # 3. Извлекаем все строки
    rows = cursor.fetchall()

    print("--- Список товаров и цен ---")
    for row in rows:
        # row[0] - это название (p.name), row[1] - это цена (pr.price)
        print(f"Товар: {row[0]:<20} | Цена: {row[1]:>8}")

except Exception as error:
    print(f"Ошибка при работе с базой данных: {error}")

finally:
    # 4. Обязательно закрываем всё, что открыли
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
    print("\nСоединение с БД закрыто.")