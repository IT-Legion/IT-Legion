# Этот код использует библиотеку Turtle для создания красивого рисунка дерева.
# Turtle - это как черепашка, которая может рисовать на экране.

import turtle  # Подключаем библиотеку Turtle, чтобы использовать её функции
import math     # Подключаем библиотеку math для математических операций (например, sin, cos)
import colorsys  # Подключаем библиотеку colorsys для работы с цветами
import random    # Подключаем библиотеку random для генерации случайных чисел

# Установка экрана
turtle.bgcolor("black")  # Задаем цвет фона (черный)
turtle.title("Искусство с помощью Turtle")  # Даем название окну

# Создание черепашки для рисования
artist = turtle.Turtle()  # Создаем черепашку и даем ей имя artist
artist.speed(0)  # Задаем скорость рисования (0 - максимальная)

# Задаем ширину линии, которой будет рисовать черепашка
artist.width(2)

# Функция для создания дерева
def draw_tree(branch_length, color_shift):
    # Если длина ветви больше 5, рисуем её
    if branch_length > 5:
        # Рассчитываем цвет ветви
        hue = (branch_length + color_shift) / 360.0
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        artist.color(color)

        # Рисуем ветвь вперед на заданную длину
        artist.pendown()
        artist.forward(branch_length)

        # Случайный порядок для ветвей
        branches = [15, -15]
        random.shuffle(branches)

        # Рисуем две новые ветви, каждая из которых будет отклоняться на случайный угол
        artist.right(branches[0])
        draw_tree(branch_length - 15, color_shift)
        artist.left(branches[0])

        artist.right(branches[1])
        draw_tree(branch_length - 15, color_shift)
        artist.left(branches[1])

        # Поднимаем перо (заканчиваем рисовать текущую ветвь)
        artist.penup()
        artist.backward(branch_length)  # Возвращаемся обратно

# Нарисовать дерево, начиная с ветви длиной 80 и без цветового сдвига
artist.left(90)  # Поворачиваем черепашку на 90 градусов влево (чтобы начать с вертикальной ветви)
draw_tree(80, 0)  # Вызываем функцию рисования дерева с начальными параметрами

# Завершение программы по клику
turtle.exitonclick()
