import unittest
from datetime import datetime
from freezegun import freeze_time
from app import hello_world  # Предполагаем, что функция, которую вы хотите протестировать, называется hello_world

class TestGetUsernameWithWeekdate(unittest.TestCase):
    
    @freeze_time("2024-05-01")  # Замораживаем дату на 1 мая 2024 года
    def test_can_get_correct_username_with_weekdate(self):
        # Проверяем для каждого из 7 дней
        dates = [
            ("2024-05-01", "Понедельник"),
            ("2024-05-02", "Вторник"),
            ("2024-05-03", "Среда"),
            ("2024-05-04", "Четверг"),
            ("2024-05-05", "Пятница"),
            ("2024-05-06", "Суббота"),
            ("2024-05-07", "Воскресенье"),
        ]
        
        for date_str, expected_day in dates:
            with self.subTest(date=date_str):
                # Получаем приветствие с учетом дня недели
                greeting = hello_world()
                # Проверяем, что день недели соответствует ожидаемому
                self.assertIn(expected_day, greeting)

if __name__ == "__main__":
    unittest.main()
