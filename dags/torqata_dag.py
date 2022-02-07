from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(dag_id="torqata_top_seller_by_state",
         start_date=datetime.today(),
         schedule_interval='0 2 * * *',
         catchup=False,
         params={'ip_schema':"torqata_data_ip",'op_schema':"torqata_data_op"}
) as dag:
     create_stg_customer_table = PostgresOperator(
             task_id="create_stg_customer_table",
             postgres_conn_id="torqata_postgres_conn",
             sql="sql/create_stg_customer.sql",
             dag=dag
             )
     insert_into_stg_customer_table = PostgresOperator(
             task_id="insert_into_stg_customer_table",
             postgres_conn_id="torqata_postgres_conn",
             sql="sql/insert_into_stg_customer.sql",
             dag=dag
             )
     create_stg_orders_table = PostgresOperator(
             task_id="create_stg_orders_table",
             postgres_conn_id="torqata_postgres_conn",
             sql="sql/create_stg_orders.sql",
             dag=dag
             )
     insert_into_stg_orders_table = PostgresOperator(
             task_id="insert_into_stg_orders_table",
             postgres_conn_id="torqata_postgres_conn",
             sql="sql/insert_into_stg_orders.sql",
             dag=dag
             )
     create_top_sellers_by_state_table = PostgresOperator(
             task_id="create_top_sellers_by_state_table",
             postgres_conn_id="torqata_postgres_conn",
             sql="sql/create_table_top_sellers_by_state.sql",
             dag=dag
             )
     create_top_sellers_by_state_archive_table = PostgresOperator(
             task_id="create_top_sellers_by_state_archive_table",
             postgres_conn_id="torqata_postgres_conn",
             sql="sql/create_table_top_sellers_by_state_archive.sql",
             dag=dag
             )
     insert_into_top_sellers_by_state_table = PostgresOperator(
             task_id="insert_into_top_sellers_by_state",
             postgres_conn_id="torqata_postgres_conn",
             sql="sql/top_sellers_by_state.sql",
             dag=dag
             )

create_stg_customer_table >> insert_into_stg_customer_table >> create_stg_orders_table >> insert_into_stg_orders_table >> create_top_sellers_by_state_table >> create_top_sellers_by_state_archive_table >> insert_into_top_sellers_by_state_table

