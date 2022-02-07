create table if not exists {{ params.ip_schema }}.stg_orders
as select * from {{ params.ip_schema }}.orders where 1=0;