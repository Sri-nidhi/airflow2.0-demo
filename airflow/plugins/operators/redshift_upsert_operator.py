import logging
from airflow.hooks.postgres_hook import PostgresHook
from airflow.plugins_manager import AirflowPlugin
from airflow.models import BaseOperator
log = logging.getLogger(__name__)

class RedshiftUpsertOperator(BaseOperator):

  def __init__(self, redshift_conn_id,
  src_table, dest_table, src_keys, dest_keys,select_query, *args, **kwargs):
    self.redshift_conn_id = redshift_conn_id
    self.src_table = src_table
    self.dest_table = dest_table
    self.src_keys = src_keys
    self.dest_keys = dest_keys
    self.select_query = select_query
    super(RedshiftUpsertOperator , self).__init__(*args, **kwargs)

  def execute(self, context):
    self.pghook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
    conn = self.pghook.get_conn()
    cursor = conn.cursor()
    log.info("Connected with " + self.redshift_conn_id)
    # build the SQL statement
    sql_statement = "begin transaction; "
    sql_statement += "delete from " + self.dest_table + " using " + self.src_table + " where "

    for i in range (0,len(self.src_keys)):
      sql_statement += self.src_table + "." + self.src_keys[i] + " = " + self.dest_table + "." + self.dest_keys[i]
      if(i < len(self.src_keys)-1):
        sql_statement += " and "

    sql_statement += "; "
    sql_statement += " insert into " + self.dest_table + self.select_query + self.src_table + " ; "
    sql_statement += " end transaction; "
    print(sql_statement)
    cursor.execute(sql_statement)
    cursor.close()
    conn.commit()
    log.info("Redshift Upsert completed")