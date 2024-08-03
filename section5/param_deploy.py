from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.models.param import Param

default_args ={
    'owner': 'airflow',
    'start_date': datetime(2024,8,3)
}

def my_task(**kwargs):
    print(kwargs)
    db=kwargs['params']['db']
    user=kwargs['params']['user']
    table=kwargs['params']['table']    
    print(f"Database Task: db:{db} , username:{user} , table:{table} ")

dag = DAG(
    'section5_params',
    default_args= default_args,
    schedule_interval=None,
    catchup=False,
    params={
        'db':'postgres',
        'table': Param('dag_run',type='string'),
        'user':'admin'
    }
)

task = PythonOperator(
    task_id='my_task',
    python_callable=my_task,
    provide_context=True,
    dag=dag
)

task