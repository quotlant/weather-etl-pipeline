import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from airflow import DAG
from scripts.extract import get_weather
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.transform import transform_weather
# from streaming.producer import producer
from streaming.producer import get_producer




default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    }
def transform_task_function(ti):
    weather_data = ti.xcom_pull(task_ids="extract_weather")
    transformed_weather = transform_weather(weather_data)
    return transformed_weather  

def producer_task_function(ti):
    transformed_weather = ti.xcom_pull( task_ids = "transform_weather")
    producer = get_producer()
    producer.send(
        "weather",
        transformed_weather 
    )
    producer.flush()
    

    
with DAG (
    dag_id ='weather_pipeline',
    start_date=datetime(2026, 8, 4),
    schedule="@hourly",
    catchup=False,
    default_args = default_args,
) as dag:
    
    extract_task = PythonOperator(
        task_id = "extract_weather",
        python_callable = get_weather,
        op_kwargs = {
            "latitude": -1.2833,
            "longitude": 36.8167,
            },
    )
    
    transform_task = PythonOperator(
        task_id = "transform_weather",
        python_callable = transform_task_function,
    )
    
    producer_task = PythonOperator(
        task_id = "producer",
        python_callable = producer_task_function
    ) 
    
    extract_task >> transform_task >> producer_task 

