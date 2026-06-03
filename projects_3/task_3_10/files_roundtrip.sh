#!/bin/bash
echo "Создаём файлы..."
for i in {1..10}; do
    filename="test${i}.txt"
    touch "$filename"
    echo "Создан файл: $filename"
done
echo "Удаляем файлы в обратном порядке..."
counter=10
while [ $counter -ge 1 ]; do
    filename="test${counter}.txt"
    if [ -f "$filename" ]; then
        rm "$filename"
        echo "Удален файл: $filename"
    else
        echo "Файл $filename не найден."
    fi
    counter=$((counter - 1))
done
echo "Все файлы обработаны."
