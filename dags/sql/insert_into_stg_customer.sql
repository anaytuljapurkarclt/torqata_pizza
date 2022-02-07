insert into {{ params.ip_schema }}.stg_customer
select * from {{ params.ip_schema }}.customer a
where not exists (select 1 from {{ params.ip_schema }}.stg_customer b
				 where a.customer_id = b.customer_id);