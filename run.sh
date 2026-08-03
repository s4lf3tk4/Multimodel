#!/bin/bash
cd "$(dirname "$0")" || exit
echo "Запуск Multimodel чата..."
if [ -d "venv" ]; then
    . venv/Scripts/activate
    python index.py
else
    echo "Отсутствует виртуальное окружение"
    echo "Запустите сначала setup.sh"
    cmd /c pause
fi
echo ""
cmd /c pause
