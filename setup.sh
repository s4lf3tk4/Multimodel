#!/bin/bash
cd "$(dirname "$0")" || exit
echo "=Установщик Multimodel ="

if ! command -v python3 &> /dev/null; then
    echo "❌ Python не найден! Установите Python 3.10+"
    cmd /c pause
fi

if [ ! -d "venv" ]; then
    echo "= Создание виртуального окружения ="
    python -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Ошибка при создании venv!"
        cmd /c pause
        exit 1
    fi
    echo "Создано OK"
else
    echo "Виртуальное окружение уже существует"
fi

echo "=Запуск виртуального окружения="

if  [ -d "venv" ]; then
    . venv/Scripts/activate
    echo "=Запущено="
else
    echo "=Виртуальное окружение на найдено="
    cmd /c pause
fi

echo "=Установка зависимостей="
if [ -f "requirements.txt" ]; then
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
else
    echo "=Не найден requirements.txt="
    cmd /c pause
fi

if [ ! -f "environment.env" ]; then
    echo ""
    echo "=ведите ваш ChatAnywhere API-ключ:"
    read -p "Ключ (sk-...): " API_KEY

    API_KEY=$(echo "$API_KEY" | sed 's/[^a-zA-Z0-9-]//g')

    if [ -z "$API_KEY" ]; then
        echo "Ключ не введён. Установка продолжена, но ключ не сохранён."
    else
        echo "CHATANYWHERE_API_KEY=$API_KEY" > environment.env
        echo "=Ключ сохранён в environment.env="
    fi
else
    echo "Файл environment.env уже существует"
fi

echo "=Установка завершена="

cmd /c pause

#rm -rf venv/
