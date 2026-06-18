from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

# Указываем Airflow искать модули внутри подпапки scripts внутри контейнера
sys.path.append('/opt/airflow/dags/scripts')

try:
    # Теперь импорт пройдет успешно, так как папка scripts добавлена в пути поиска
    from build_mart import create_mart as run_analytics_calculation
except ImportError as e:
    def run_analytics_calculation():
        raise RuntimeError(f"Не удалось найти build_mart.py в папе dags/scripts. Ошибка: {e}")

default_args = {
    'owner': 'Kashin',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'create_analytics_mart',
    default_args=default_args,
    description='DAG для запуска расчета аналитической витрины из папки scripts',
    schedule_interval=None,  # Ручной запуск
    catchup=False,
) as dag:

    execute_analytics_migration = PythonOperator(
        task_id='execute_analytics_migration',
        python_callable=run_analytics_calculation,
    )

    execute_analytics_migration