#!/bin/bash
for i in {1..20}; do
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
    if [ $i -eq 15 ]; then
        echo "Встречено число 15, останавливаем работу."
        break
    fi
    echo "Нечётное число: $i"
done
echo "Скрипт завершён."
