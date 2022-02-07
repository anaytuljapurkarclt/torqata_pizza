create table if not exists {{ params.ip_schema }}.stg_customer
as select * from {{ params.ip_schema }}.customer where 1=0;
