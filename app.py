# Импорт класса Flask из библиотеки Flask и функции render_template для рендеринга HTML-шаблонов
from flask import Flask, render_template  


# Создание экземпляра веб-приложения Flask с указанием текущего модуля в качестве имени
app = Flask(__name__)



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


# Декоратор для установки маршрута '/partners'' для вызова функции partners
@app.route('/partners')
def partners():  
    # Функция для отображения страницы о нас 
    return render_template('main/partners.html') 



@app.route('/informatics')
def informatics_main():

    return render_template('/content/informatics/informatics.html')

# Декоратор для установки маршрута '/partners'' для вызова функции partners
@app.route('/information_concept')
def information_concept():  
    # Функция для отображения страницы о нас 
    return render_template('/content/informatics/information_concept.html') 


# Декоратор для установки маршрута '/partners'' для вызова функции partners
@app.route('/1')
def main():  
    # Функция для отображения страницы о нас 
    return render_template('/1.html') 







# Условие для проверки, запущен ли этот скрипт напрямую
if __name__ == '__main__':  
    # Запуск веб-приложения Flask в режиме отладки
    app.run(debug=True)  