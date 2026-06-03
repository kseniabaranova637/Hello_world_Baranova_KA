-- Объединенный запрос для получения всей статистики сразу
SELECT 
    product_id, 
    COUNT(*) AS total_records,   -- Количество записей
    AVG(price) AS average_price, -- Средняя цена
    MIN(price) AS min_price,     -- Минимальная цена
    MAX(price) AS max_price      -- Максимальная цена
FROM prices
GROUP BY product_id;

-- Если вам нужны отдельные запросы для каждой задачи:

-- 1. Количество записей для каждого товара
SELECT product_id, COUNT(*) FROM prices GROUP BY product_id;

-- 2. Средняя цена для каждого товара
SELECT product_id, AVG(price) FROM prices GROUP BY product_id;

-- 3. Минимальная цена для каждого товара
SELECT product_id, MIN(price) FROM prices GROUP BY product_id;

-- 4. Максимальная цена для каждого товара
SELECT product_id, MAX(price) FROM prices GROUP BY product_id;