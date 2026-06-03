#!/bin/bash
echo -e "Ivan 78\nMaria 92\nOleg 67\nAnna 85" > students.txt
echo "Имена студентов:"
awk '{print $1}' students.txt

echo -e "\nОценки:"
awk '{print $2}' students.txt

echo -e "\nНомер строки и имя:"
awk '{print NR, $1}' students.txt
