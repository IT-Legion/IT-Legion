#!/bin/bash

# Получаем имя текущего пользователя
current_user=$(whoami)

# Определяем путь к рабочему столу в зависимости от операционной системы
case "$OSTYPE" in
    linux-gnu*)
        desktop_path="/home/$current_user/Рабочий стол"
        ;;
    darwin*)
        desktop_path="/Users/$current_user/Desktop"
        ;;
    *)
        echo "Error: Unsupported operating system"
        exit 1
        ;;
esac

# Переходим на рабочий стол
cd "$desktop_path" || { echo "Error: Unable to change directory to $desktop_path"; exit 1; }

# Клонируем репозиторий
git clone https://github.com/IT-Legion/my-website-on-flask.git

# Проверяем наличие каталога и выполняем нужные команды
if [ -d "my-website-on-flask" ]; then
    cd my-website-on-flask
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    flask run
else
    echo "Error: Directory 'my-website-on-flask' not found."
fi
