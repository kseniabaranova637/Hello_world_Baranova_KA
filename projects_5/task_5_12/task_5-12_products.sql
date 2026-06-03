-- 1. Количество товаров с группировкой по категориям
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category;

-- 2. Количество товаров в каждой категории с сортировкой по убыванию
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC;