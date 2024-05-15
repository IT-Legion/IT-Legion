import json
# Импортируем класс Flask из библиотеки Flask и необходимые функции
from flask import Flask, render_template, jsonify, make_response, redirect, url_for, request, session 
import datetime

# Создаем экземпляр веб-приложения Flask
app = Flask(__name__)

# Устанавливаем секретный ключ для защиты сессий
app.config['SECRET_KEY'] = "e6a07d016fec9deab0f118b09e3f9220aae757d4"
# Устанавливаем время жизни сессии
app.permanent_session_lifetime = datetime.timedelta(days=1)



@app.route('/html_info')
def html_info():
    string = ""
    with open('templates/main/html_info.json', 'r') as file:
        html_info_data = json.load(file)
        print(type(html_info_data["lesson topics"]))
        for topic, details in html_info_data["lesson topics"].items():
            print(topic)
            print(details)
            string += f"\n{topic}: {details}<br>"
            print(string)
    print(string)

    return string



# Декоратор маршрута для обработки запросов к домашним заданиям участников
@app.route('/<path:surname>/<name>')
def homework(surname, name):
    # Проверяем, является ли имя страницы одним из стандартных: 'home', 'about', 'partners'
    if name in ('home', 'about', 'partners'):
        # Если да, перенаправляем на соответствующий маршрут
        return redirect(f'/{name}')
    
    try:
        # Пытаемся отрендерить HTML-шаблон для указанной фамилии и имени
        return render_template(f'/homework/{surname}/{name}.html')
    except:
        # Если не удается найти шаблон, возвращаем ошибку 404
        return "404 Файл данного ученика не найден. 404"

# Декоратор маршрута для главной страницы
@app.route('/home')
@app.route('/')
def index():  
    # Функция для отображения главной страницы приложения
    return render_template('main/index.html')   

# Декоратор маршрута для страницы "О нас"
@app.route('/about')
def about():  
    # Функция для отображения страницы "О нас"
    return render_template('main/about.html')

# Декоратор маршрута для страницы "Партнеры"
@app.route('/partners')
def partners():  
    # Функция для отображения страницы "Партнеры"
    return render_template('main/partners.html') 

# Декоратор маршрута для страницы информатики
@app.route('/informatics')
def informatics_main():
    # Функция для отображения страницы информатики
    return render_template('/content/informatics_room/informatics.html')

# Декоратор маршрута для страницы концепции информации
@app.route('/information_concept')
def information_concept():  
    # Функция для отображения страницы концепции информации
    return render_template('/content/informatics_room/information_concept.html')

# Декоратор маршрута для страницы тестирования по информатике
@app.route('/cst')
def computer_science_test():
    # Функция для отображения страницы тестирования по информатике
    return render_template('/content/informatics_room/cst.html')

# Декоратор маршрута для страницы тестирования билетов по информатике
@app.route('/cst2')
def computer_science_tickets():
    # Функция для отображения страницы тестирования билетов по информатике
    return render_template('/content/informatics_room/cst2.html')

# Декоратор маршрута для гостевой комнаты по Python
@app.route('/guest_room_python')
def guest_room():
    # Функция для отображения гостевой комнаты по Python
    return render_template('/content/python_room/main_in_python.html')

# Декоратор маршрута для гостевой комнаты по космосу
@app.route('/guest_room_space')
def guest_space():
    # Функция для отображения гостевой комнаты по космосу
    return "<a href='https://sonik.space/'>sonik</a>  <a href=''></a>  <a href='https://www.google.com/earth/studio/'>earth/studio/</a> https://introsat.ru/"

# Декоратор маршрута для страниц уроков по Python
@app.route('/lesson/<int:id>')
def lesson_py(id):  
    # Функция для отображения страницы уроков по Python
    return render_template(f'content/python_room/lesson_{id}.html') 

# Декоратор маршрута для страницы инициализации в проекте
@app.route('/init_in_project')
def init_in_project():
    # Функция для отображения страницы инициализации в проекте
    return render_template('content/git_room/init_in_project.html')

# Декоратор маршрута для страницы заметок по Python
@app.route('/python-notes/<int:id>')
def python_notes(id):
    # Функция для отображения страницы заметок по Python
    if id == 1:
        return render_template('/content/python_room/notes/telebot.html')

# Декоратор маршрута для страницы заметок по Python
@app.route('/git')
def git():
    # Функция для отображения страницы заметок по Python
    return render_template('/content/git_room/main_in_git.html')


    



# Декоратор маршрута для тестовой страницы
@app.route('/test')
def test():
    # Увеличиваем счетчик посещений при каждом обращении к странице
    if "visits" in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return f"Число просмотров: {session['visits']} "

# Пример сессии
data = [1, 2, 3, 4]
@app.route('/example')
def for_example_session():
    # Устанавливаем сессию как постоянную
    session.permanent = True
    # Если данные еще не были сохранены в сессии
    if 'data' not in session:
        session['data'] = data
    else:
        # Увеличиваем второй элемент списка на единицу
        session['data'][1] += 1
        # Указываем, что данные в сессии были изменены
        session.modified = True
    return f"<p>session['data']: {session['data']}"

#Пример запроса
@app.route('/hello-world/<name>')
def hello_world(name):
    # Словарь с переводом дней недели на русский
    weekday_translation = {
    'monday': 'понедельника',
    'tuesday': 'вторника',
    'wednesday': 'среды',
    'thursday': 'четверга',
    'friday': 'пятницы',
    'saturday': 'субботы',
    'sunday': 'воскресенья'
}
    # Получаем текущий день недели на английском
    weekday_en = datetime.datetime.now().strftime('%A').lower()
    # Переводим текущий день недели на русский
    weekday_ru = weekday_translation.get(weekday_en, 'день недели')
    # Формируем пожелание на русском языке
    if weekday_ru[-1] == 'ы':
        wish_ru = f'Хорошей {weekday_ru}!'
    else:
        wish_ru = f'Хорошего {weekday_ru}!'
    return f'Привет, {name}. {wish_ru}'


# Запускаем приложение, если файл запущен напрямую
if __name__ == '__main__':
    # Запускаем веб-приложение Flask в режиме отладки
    app.run(debug=True)
