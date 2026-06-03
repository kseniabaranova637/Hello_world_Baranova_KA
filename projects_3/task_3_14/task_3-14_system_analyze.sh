#!/bin/bash

echo "Анализ использования дискового пространства:"
df -h | awk '
NR > 1 {
    fs = $1
    percent = $5
    gsub("%", "", percent)
    print fs, $5
    if (percent > 90) {
        print "ПРЕДУПРЕЖДЕНИЕ: " fs " заполнено на " percent "%" > "/dev/stderr"
    }
}
'
