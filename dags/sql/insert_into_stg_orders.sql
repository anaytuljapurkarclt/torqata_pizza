truncate table {{ params.ip_schema }}.stg_orders;

insert into {{ params.ip_schema }}.stg_orders
select * from {{ params.ip_schema }}.orders
where order_date::date
between ((current_date + interval '-1' day) at time zone 'utc' + interval '-1' year)
and	((current_date + interval '-1' day) at time zone 'utc');