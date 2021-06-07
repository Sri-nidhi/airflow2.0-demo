#!/usr/bin/env bash
echo $AIRFLOW_HOME

# Setup DB Connection String
AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN

AIRFLOW__WEBSERVER__SECRET_KEY="openssl rand -hex 30"
export AIRFLOW__WEBSERVER__SECRET_KEY

#DBT_POSTGRESQL_CONN="postgresql+psycopg2://${DBT_POSTGRES_USER}:${DBT_POSTGRES_PASSWORD}@${DBT_POSTGRES_HOST}:${POSTGRES_PORT}/${DBT_POSTGRES_DB}"

cd /dbt && dbt compile
rm -f /airflow/airflow-webserver.pid
pip install -r /project/scripts/requirements.txt 
sleep 10
FLASK_APP=airflow.www.app flask fab create-admin --username admin --email admin@example.com --firstname admin --lastname user --password demo
airflow db upgrade
sleep 10
airflow info
airflow connections add redshift_land --conn-host "redshift-cluster-2.cmwaeomvtjzi.us-east-2.redshift.amazonaws.com" --conn-schema "dev" --conn-login "awsuser" --conn-password "Dynamics238" -conn-port "5439"
airflow connections add aws_id --conn-type aws --conn-extra \'{"AWS_ACCESS_KEY_ID": ${AWS_ACCESS_ID},"AWS_SECRET_ACCESS_KEY": ${AWS_SECRET_ID}\'
airflow connections add s3_conn --conn-type s3 --conn-extra \'{"AWS_ACCESS_KEY_ID": ${AWS_ACCESS_ID},"AWS_SECRET_ACCESS_KEY": ${AWS_SECRET_ID}\'

airflow scheduler & airflow webserver