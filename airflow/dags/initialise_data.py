from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from helpers.create_tables import *
from airflow.utils.task_group import TaskGroup

# [START default_args]
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

stages = [
    {"task_name": "create_schemas",
     "sql": create_schemas},
    {"task_name": "create_staging_tables",
         "sql": create_staging_tables},
    {"task_name": "create_curated_tables",
         "sql": create_curated_tables},
    {"task_name": "create_datamart_tables",
         "sql": create_datamart_tables}
]
task = {}

with DAG('load_initial_data',
          default_args=default_args,
          description='Create Redshift tables',
          schedule_interval=None,
          max_active_runs=1,
          tags=['demo']
        ) as dag:

    create_ddl = DummyOperator(task_id="create_ddl_group")

    with TaskGroup(group_id='ddl') as create_tables:
        for i in range(0, len(stages)):
            task[i] = PostgresOperator(task_id= stages[i]["task_name"], postgres_conn_id="redshift_land",sql= stages[i]["sql"])
            if i > 0:
                task[i - 1].set_downstream(task[i])


create_ddl >> create_tables