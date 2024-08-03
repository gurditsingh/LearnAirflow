# Apache Airflow `default_args` Names and Example Values

This file lists the common `default_args` parameters used in Apache Airflow DAGs along with their example values.

## Default Args Names and Example Values

| **Parameter**           | **Example Value**              | **Description**                                                      |
|-------------------------|--------------------------------|----------------------------------------------------------------------|
| `owner`                 | `'airflow'`                     | Specifies the owner of the task.                                    |
| `depends_on_past`       | `False`                         | When set to `True`, a task instance runs only if the previous task instance in the previous DAG run succeeded. |
| `start_date`            | `datetime(2023, 1, 1)`          | The start date for the DAG. Task instances will be triggered from this date onwards. |
| `email`                 | `['example@example.com']`       | A list of email addresses to notify if a task fails.                 |
| `email_on_failure`      | `True`                          | When set to `True`, email notifications will be sent if a task fails. |
| `email_on_retry`        | `False`                         | When set to `True`, email notifications will be sent if a task is retried. |
| `retries`               | `1`                             | The number of retries that should be performed before failing the task. |
| `retry_delay`           | `timedelta(minutes=5)`          | The time delay between retries.                                      |
| `end_date`              | `datetime(2023, 12, 31)`        | The end date for the DAG. No tasks will be scheduled after this date. |
| `execution_timeout`     | `timedelta(hours=1)`            | The maximum time allowed for the execution of the task.              |
| `on_failure_callback`   | `some_function`                 | A callback function that is executed when a task fails.              |
| `on_success_callback`   | `some_function`                 | A callback function that is executed when a task succeeds.           |
| `on_retry_callback`     | `some_function`                 | A callback function that is executed when a task is retried.         |
| `provide_context`       | `True`                          | When set to `True`, passes a set of context variables to the task instances. |

## Example DAG with `default_args`

Here’s an example of a simple DAG using `default_args`:

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

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
    'provide_context': True,
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end
