#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- 1. Таблица логов
    CREATE TABLE IF NOT EXISTS user_logs (
        courseid INTEGER,
        userid INTEGER,
        num_week INTEGER,
        s_all INTEGER,
        s_all_avg VARCHAR(255),
        s_course_viewed INTEGER,
        s_course_viewed_avg VARCHAR(255),
        s_q_attempt_viewed INTEGER,
        s_q_attempt_viewed_avg VARCHAR(255),
        s_a_course_module_viewed INTEGER,
        s_a_course_module_viewed_avg VARCHAR(255),
        s_a_submission_status_viewed INTEGER,
        s_a_submission_status_viewed_avg VARCHAR(255),
        NameR_Level VARCHAR(255),
        Name_vAtt VARCHAR(255),
        "Depart" VARCHAR(255), -- Кавычки нужны, если в CSV заголовок с большой буквы
        Name_OsnO VARCHAR(255),
        Name_FormOPril VARCHAR(255),
        LevelEd VARCHAR(255),
        Num_Sem INTEGER,
        Kurs INTEGER,
        Date_vAtt VARCHAR(255)
    );

    -- 2. Таблица кафедр (ДЛЯ ЗАДАНИЯ)
    CREATE TABLE IF NOT EXISTS departments (
        Depart INTEGER,
        department_name VARCHAR(255)
    );

    -- 3. Загрузка данных (Используем COPY без слэша)
    COPY user_logs FROM '/datasets/aggrigation_logs_per_week.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
    
    -- Убедитесь, что файл departments.csv лежит в папке datasets
    COPY departments FROM '/datasets/departments.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');

    -- 4. Преобразование типа Depart в integer (КАК В ЗАДАНИИ)
    ALTER TABLE user_logs ALTER COLUMN "Depart" TYPE integer USING "Depart"::integer;

EOSQL




