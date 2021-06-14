from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from helpers.create_tables import *
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
from helpers.alert import task_success_alert, task_failure_alert
# from functools import partial
from airflow.models import Variable
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
# [START default_args]

default_args = {
    'owner': 'srinidhi',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'on_failure_callback': task_failure_alert,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}


full_refresh = Variable.get("full_refresh")
# def check_trigger(context, dag_run_obj):
#     if full_refresh.lower() == 'y':
#         return dag_run_obj

stages = [
    {"task_name": "create_schemas",
     "sql": create_schemas},
{"task_name": "create_landing_tables",
         "sql": create_landing_tables}

]
task = {}
# send_success_notification = partial(task_success_alert)modes
with DAG('create_landing_tables',
          default_args=default_args,
          description='Create Redshift tables',
          schedule_interval=None,
          max_active_runs=1,
          tags=['demo']
        ) as dag:


    with TaskGroup(group_id='ddl') as create_tables:
        for i in range(0, len(stages)):
            task[i] = PostgresOperator(task_id= stages[i]["task_name"], postgres_conn_id="redshift_land",sql= stages[i]["sql"])
            if i > 0:
                task[i - 1].set_downstream(task[i])

    trigger = TriggerDagRunOperator(
        task_id='start_s3_load',
        trigger_dag_id="S3toRedshift_Ingestion",
        dag=dag)

create_tables >> trigger