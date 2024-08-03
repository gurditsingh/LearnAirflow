from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.models.param import Param

def print_params(**kwargs):
    params = kwargs.get('params', {})
    print(f"Param1: {params.get('param1', 'default_value')}")
    print(f"Param2: {params.get('param2', 0)}")
    print(f"Param3: {params.get('param3', [])}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

dag = DAG(
    'dag_with_params',
    default_args=default_args,
    description='A DAG with params for tasks',
    schedule_interval=None,
    params={
        'param1': Param('default_value', type='string', description='A string parameter'),   # DAG level
        'param2': 42,
        'param3': [1, 2, 3]
    }
)

print_params_task = PythonOperator(
    task_id='print_params_task',
    python_callable=print_params,
    provide_context=True,
    params={
        'param1': Param('task_value', type='string', description='A string parameter'),  # Task level
        'param2': 99
    },
    dag=dag
)

print_params_bash_task = BashOperator(
    task_id='print_params_bash_task',
    bash_command="""echo "Param1: {{ params.param1 }}"
                    echo "Param2: {{ params.param2 }}"
                    echo "Param3: {{ params.param3 }}" """,
    params={
        'param1': Param('bash_value', type='string', description='A string parameter')   # Task level
    },
    dag=dag
)

print_params_task
print_params_bash_task
