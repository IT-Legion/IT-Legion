# Импорт класса Flask из библиотеки Flask и функции render_template для рендеринга HTML-шаблонов
# Импорт функции url_for для создания URL-адресов
from flask import Flask, render_template, url_for 
from flask_sqlalchemy import SQLAlchemy

# Создание экземпляра веб-приложения Flask с указанием текущего модуля в качестве имени
app = Flask(__name__)

#app.config['']



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
    return render_template('/content/informatics/informatics.html')


# Декоратор для установки маршрута '/information_concept' для вызова функции partners
@app.route('/information_concept')
def information_concept():  
    # Функция для отображения страницы о нас 
    return render_template('/content/informatics/information_concept.html') 



# Обратите внимание! На адресную строку и путь до файла Добро пожаловать, дорогие гости!
#Старт: В Welcome шаблон:->>

@app.route('/guest_room_python')
def guest_room():
    
    return render_template('content/python/main_in_python.html')

#<--В Welcome шаблон:<<--
@app.route('/space_room')
def guest_space():

    return "<a href='https://sonik.space/'>sonik</a>  <a href='https://www.google.com/earth/studio/'>earth/studio/</a>"   
#-->В Welcome шаблон:->>#end:
#
#       Шаблон!
#-->В Welcome шаблон:-->
#
# <--В Welcome шаблон:<<--





@app.route('/lesson/<int:id>')
def lesson_py(id):  
    # Функция для отображения страниц lesson
    return render_template(f'/content/python/lesson_{id}.html') 






# Декоратор для установки маршрута '/дз диана' для вызова функции 
@app.route('/1')
def diana():  
    # Функция для отображения страницы о нас 
    return render_template('/homework/1.html') 



# Декоратор для установки маршрута '/дз рома' для вызова функции 
@app.route('/2')
def roma():  
    # Функция для отображения страницы о нас 
    return render_template('/homework/1.html') 

@app.route('/3')
def stepan():

    return render_template('/homework/stepan.html')


@app.route('/maksim')
def maksim():

    return render_template('/homework/maksim.html')

@app.route('/5')
def nikita():

    return render_template('/homework/nikita.html')

@app.route('/6')
def polina():

    return render_template('/homework/polina.html')

@app.route('/7')
def sofa():

    return render_template('/homework/sofa.html')

@app.route('/8')
def vlad():

    return render_template('/homework/vlad.html')


@app.route('/9')
def vova():

    return render_template('/homework/vova.html')


@app.route('/test')
def test():

    return render_template('content/web/HTML/base_html.html')






# Условие для проверки, запущен ли этот скрипт напрямую
if __name__ == '__main__':  
    # Запуск веб-приложения Flask в режиме отладки
    app.run(debug=True)  