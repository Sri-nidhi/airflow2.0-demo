from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from helpers.alert import task_success_alert, task_failure_alert
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

default_args = {
    'owner': 'srinidhi',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'on_failure_callback': task_failure_alert
}

dag = DAG(
    'basic_dag2',
    default_args=default_args,
    description='Creating a Simple DAG',
    schedule_interval = None,
)

#
def setup_var_and_xcom(**context):
    iterator = Variable.get('basic_dag_var', default_var='N')
    context['ti'].xcom_push(key='important_xcom_value', value = iterator)



# basic = DummyOperator(
#     task_id='dummy_task',
#     dag=dag
# )



task1 = PythonOperator(
    task_id='task1',
    python_callable=setup_var_and_xcom,
    provide_context=True,
    dag=dag
)
# #
def get_xcom(**context):
    msg = context['ti'].xcom_pull(key="important_xcom_value")
    print("Task Message:{}".format(msg))

#
task2 = PythonOperator(
    task_id='task2',
    python_callable= get_xcom,
    provide_context=True,
    dag=dag
)
#
task1 >> task2
