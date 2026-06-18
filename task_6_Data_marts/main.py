"""
 Требуется создать отдельную схему dmr  (Data Mart Repository) для аналитических данных и 
 разместить в ней витрину analytics_student_performancee.

 Требования:
- Создать схему dmr если она не существует
- Создать витрину dmr.analytics_student_performance с агрегированными данными.
- Реализация через функции

Структура витрины: 
Поле	- Тип данных	- Описание
student_id	- INTEGER	- ID студента
course_id -	INTEGER	ID - курса
department_id -	INTEGER	- Код кафедры
department_name	 - VARCHAR - Название кафедры
education_level	- VARCHAR	- Уровень образования
education_base - VARCHAR -	Основа обучения
semester	- INTEGER	- Номер семестра
course_year	- INTEGER	- Курс обучения
final_grade -	INTEGER -	Итоговая оценка
total_events -	INTEGER	- Всего событий за семестр
avg_weekly_events	- DECIMAL(10,2)	- Среднее событий в неделю
total_course_views	- INTEGER	- Всего просмотров курса
total_quiz_views	- INTEGER	- Всего просмотров тестов
total_module_views -	INTEGER - Всего просмотров модулей
total_submissions	- INTEGER	- Всего отправленных заданий
peak_activity_week	- INTEGER	- Неделя с максимальной активностью
consistency_score	- DECIMAL(5,2)	- Коэффициент стабильности активности (0-1)
activity_category	- VARCHAR	- Категория активности (низкая/средняя/высокая)
last_update	- TIMESTAMP	- Дата обновления записи

"""


# Ниже представлен пример реализации витрины dmr.analytics_student
# Поле	- Тип данных	- Описание
# student_id	- INTEGER	- ID студента
# course_id -	INTEGER	ID - курса
# department_id -	INTEGER	- Код кафедры
# semester	- INTEGER	- Номер семестра
# course_year	- INTEGER	- Курс обучения
# final_grade -	INTEGER -	Итоговая оценка
# last_update	- TIMESTAMP	- Дата обновления записи

import os
import sys
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('DB_HOST', 'localhost'),
        'port': os.getenv('DB_PORT', '15432'),  
        'database': os.getenv('DB_NAME', 'my_db_Kashin'),
        'user': os.getenv('DB_USER', 'Kashin'),
        'password': os.getenv('DB_PASSWORD', 'Super_Strong_Pass_2026!_')
    }

def get_connection():
    try:
        config = get_db_config()
        conn = psycopg2.connect(**config)
        conn.autocommit = True
        return conn
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")
        sys.exit(1)

def main():
    conn = None
    try:
        print("Запуск процесса обновления витрины через встроенную PL/pgSQL функцию...")
        conn = get_connection()
        with conn.cursor() as cur:
            # Вызов функции, которую мы определили в БД
            cur.execute("SELECT dmr.refresh_student_performance();")
            print("Витрина dmr.analytics_student_performance успешно обновлена!")
    except Exception as e:
        print(f"Критическая ошибка при обновлении витрины: {e}")
    finally:
        if conn:
            conn.close()
            print("Соединение с БД закрыто.")

if __name__ == "__main__":
    main()