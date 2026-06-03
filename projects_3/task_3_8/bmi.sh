#!/bin/bash
echo -n "Введите ваш вес в кг: "
read WEIGHT
echo -n "Введите рост в см: "
read HEIGHT
HEIGHT_SQUARED=$((HEIGHT * HEIGHT))
BMI=$((WEIGHT / HEIGHT_SQUARED))
echo "Ваш ИМТ: $BMI"
