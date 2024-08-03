# Apache Airflow DAG Arguments

This file lists common arguments used when defining a DAG in Apache Airflow, along with their example values.

## DAG Arguments and Example Values

| **Argument**             | **Example Value**             | **Description**                                                      |
|--------------------------|-------------------------------|----------------------------------------------------------------------|
| `dag_id`                 | `'example_dag'`               | A unique identifier for the DAG.                                    |
| `description`            | `'A sample DAG for demonstration purposes.'` | A description of what the DAG does.                                |
| `schedule_interval`      | `timedelta(days=1)`           | The frequency with which the DAG should be run. Can also be a CRON expression or `'@daily'`. |
| `start_date`             | `datetime(2023, 1, 1)`        | The start date for the DAG. Tasks will start running from this date. |
| `end_date`               | `datetime(2023, 12, 31)`      | The end date for the DAG. No tasks will be scheduled after this date. |
| `default_args`           | `{...}`                       | A dictionary of default arguments applied to all tasks in the DAG.  |
| `catchup`                | `True`                        | When set to `True`, the DAG will catch up on missed runs between the `start_date` and now. |
| `tags`                   | `['example', 'demo']`         | A list of tags to categorize and filter DAGs in the Airflow UI.      |
| `params`                 | `{'param1': 'value1'}`        | A dictionary of parameters that can be used by tasks in the DAG.     |
| `max_active_runs`        | `1`                           | The maximum number of active DAG runs at any given time.            |
| `concurrency`            | `5`                           | The maximum number of tasks that can run simultaneously for this DAG. |
| `dagrun_timeout`         | `timedelta(hours=2)`          | The maximum duration that a DAG run is allowed to execute.           |
| `on_failure_callback`    | `some_function`               | A callback function that is executed when any task in the DAG fails. |
| `on_success_callback`    | `some_function`               | A callback function that is executed when any task in the DAG succeeds. |
| `on_retry_callback`      | `some_function`               | A callback function that is executed when any task in the DAG is retried. |
| `sla_miss_callback`      | `sla_miss_function`           | A callback function that is executed when a task in the DAG misses its SLA. |

## Example DAG

Here’s an example of a simple DAG using various arguments:

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

def sla_miss_callback(dag, task_list, blocking_task_list, slas, blocking_tis):
    # Example SLA miss callback function
    print(f"SLA missed for DAG: {dag.dag_id}")
    print(f"Tasks: {task_list}")
    print(f"Blocking Tasks: {blocking_task_list}")
    print(f"SLAs: {slas}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['example@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=1),
}

dag = DAG(
    'example_dag',
    description='An example DAG with various arguments',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2023, 12, 31),
    default_args=default_args,
    catchup=False,
    tags=['example', 'demo'],
    params={'param1': 'value1'},
    max_active_runs=1,
    concurrency=5,
    dagrun_timeout=timedelta(hours=2),
    on_failure_callback=lambda context: print('DAG failed'),
    on_success_callback=lambda context: print('DAG succeeded'),
    on_retry_callback=lambda context: print('DAG retry'),
    sla_miss_callback=sla_miss_callback,
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end
