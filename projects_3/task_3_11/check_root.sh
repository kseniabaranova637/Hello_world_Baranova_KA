#!/bin/bash
check_root() {
    if [ $EUID -ne 0 ]; then
        echo "Ошибка: скрипт должен быть запущен от имени root!"
        exit 1
    fi
}
check_root
echo "Успех: скрипт запущен от имени root."
