# Импорт класса Flask из библиотеки Flask и функции render_template для рендеринга HTML-шаблонов
# Импорт функции url_for для создания URL-адресов
from flask import Flask, render_template,redirect, url_for 
#from flask_sqlalchemy import SQLAlchemy

# Создание'home' экземпляра веб-приложения Flask с указанием текущего модуля в качестве имени
app = Flask(__name__)

#app.config['']

#====ВНИМАНИЕ!====
# Декоратор для установки маршрута к домашним заданиям:
# Участники!
@app.route('/<path:surname>/<name>')  # Определяем маршрут, который принимает два параметра: фамилию и имя.
def homework(surname, name):
    print(type(name))
    if name in ('home','about','partners'):
        return redirect(f'/{name}')

    try:  # Начинаем блок try-except для обработки возможного исключения.
        # Пытаемся отрендерить шаблон для указанной фамилии и имени.
        return render_template(f'/homework/{surname}/{name}.html')
    except:  # Если возникает исключение...
        return "404 Файл данного ученика не найден. 404"  # ...возвращаем сообщение о том, что файл не найден.
#====ВНИМАНИЕ!====



# Декоратор для установки маршрута '/' для вызова функции index
@app.route('/home')
@app.route('/')
def index():  
    # Функция для отображения главной страницы приложения
    return render_template('main/index.html')   



# Декоратор для установки маршрута '/about' для вызова функции about
@app.route('/about')
def about():  
    # Функция для отображения страницы о нас 
    return render_template('main/about.html')   


# Декоратор для установки маршрута '/partners' для вызова функции partners
@app.route('/partners')
def partners():  
    # Функция для отображения страницы о нас 
    return render_template('main/partners.html') 


# Декоратор для установки маршрута '/information_concept' для вызова функции partners
@app.route('/informatics')
def informatics_main():
    # Функция для отображения страницы
    return render_template('/content/informatics_room/informatics.html')


# Декоратор для установки маршрута '/information_concept' для вызова функции partners
@app.route('/information_concept')
def information_concept():  
    # Функция для отображения страницы о нас 
    return render_template('/content/informatics_room/information_concept.html') 

@app.route('/cst')
def computer_science_test():

    return render_template('/content/informatics_room/cst.html')

@app.route('/cst2')
def computer_science_tickets():

    return render_template('/content/informatics_room/cst2.html')

# Обратите внимание! На адресную строку и путь до файла Добро пожаловать, дорогие гости!
#Старт: В Welcome шаблон:->>

@app.route('/guest_room_python')
def guest_room():
    
    return render_template('/content/python_room/main_in_python.html')

#<--В Welcome шаблон:<<--
@app.route('/guest_room_space')
def guest_space():

    return "<a href='https://sonik.space/'>sonik</a>  <a href=''></a>  <a href='https://www.google.com/earth/studio/'>earth/studio/</a> https://introsat.ru/"   
#-->В Welcome шаблон:->>#end:
#
#       Шаблон!
#-->В Welcome шаблон:-->
#
# <--В Welcome шаблон:<<--

@app.route('/lesson/<int:id>')
def lesson_py(id):  
    # Функция для отображения страниц lesson
    return render_template(f'content/python_room/lesson_{id}.html') 


# Декоратор для установки маршрута Инициализация в проекте
@app.route('/init_in_project')
def init_in_project():
    # Функция для отображения страницы
    return render_template('content/git_room/init_in_project.html')



@app.route('/python-notes/<int:id>')
def python_notes(id):
    if id == 1:
        return render_template('/content/python_room/notes/telebot.html')








@app.route('/test/test')
def test():
    # Функция для отображения страницы
    return redirect('/home')

    #return render_template('/test.html')



# Условие для проверки, запущен ли этот скрипт напрямую
if __name__ == '__main__':  
    # Запуск веб-приложения Flask в режиме отладки
    app.run(debug=True)  