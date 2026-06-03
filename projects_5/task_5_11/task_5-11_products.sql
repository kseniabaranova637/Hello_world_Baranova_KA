-- 1. Товары из категории «Электроника»
SELECT * FROM products 
WHERE category = 'Электроника';

-- 2. Товары из категории «Одежда» со словом «женские» в названии
SELECT * FROM products 
WHERE category = 'Одежда' AND name ILIKE '%женские%';

-- 3. Товары категорий «Продукты» или «Книги»
SELECT * FROM products 
WHERE category IN ('Продукты', 'Книги');

-- 4. Все товары, кроме категории «Бытовая техника»
SELECT * FROM products 
WHERE category != 'Бытовая техника';

-- 5. Товары из списка категорий: «Электроника», «Одежда», «Книги»
SELECT * FROM products 
WHERE category IN ('Электроника', 'Одежда', 'Книги');

-- 6. Электроника Samsung ИЛИ Бытовая техника
SELECT * FROM products 
WHERE (category = 'Электроника' AND name ILIKE '%Samsung%')
   OR (category = 'Бытовая техника');

-- 7. Сложное условие с диапазоном ID и исключением слова Samsung
SELECT * FROM products 
WHERE (
    category IN ('Электроника', 'Одежда', 'Бытовая техника') 
    AND id BETWEEN 1 AND 15 
    AND name NOT ILIKE '%Samsung%'
) OR (category = 'Книги');