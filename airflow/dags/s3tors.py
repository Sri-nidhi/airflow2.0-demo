from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow import DAG
from datetime import datetime
from operators.redshift_upsert_operator import RedshiftUpsertOperator
from helpers.sql_queries import DataValidation
from datetime import datetime, timedelta


default_args = {
    'owner': 'srinidhi',
    'depends_on_past': False,
    'start_date': datetime(2019, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG('S3toRedshift_Ingestion',
          default_args=default_args,
          schedule_interval='@hourly',
          catchup=False,
          tags=['demo'])

load_to_land1 = S3ToRedshiftOperator(
        task_id='load_to_land1',
        schema='analytics',
        table='covid_cases',
        s3_bucket='apache-airflow-assets',
        s3_key='Input/covid_cases',
        copy_options=['csv'],
        aws_conn_id='aws_id',
        redshift_conn_id='redshift_land',
        dag = dag
)

load_to_land2 = S3ToRedshiftOperator(
        task_id='load_to_land2',
        schema='analytics',
        table='state_tests',
        s3_bucket='apache-airflow-assets',
        s3_key='Input/state_tests',
        copy_options=['csv'],
        aws_conn_id='aws_id',
        redshift_conn_id='redshift_land',
        dag = dag
)

load_to_land1
load_to_land2