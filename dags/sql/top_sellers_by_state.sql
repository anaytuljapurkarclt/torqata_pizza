insert into {{ params.op_schema }}.top_sellers_by_state_archive 
select * from {{ params.op_schema }}.top_sellers_by_state;

TRUNCATE TABLE {{ params.op_schema }}.top_sellers_by_state;

with cust_ordr_itm_more_than_once as
(
	select c.state, o.type,c.customer_id, count(*)
	from {{ params.ip_schema }}.stg_orders o
	inner join {{ params.ip_schema }}.stg_customer c
		on o.customer_id = c.customer_id
	group by 1,2,3
	having count(*)>=1
)
,main as (
	select
		c.state
		,o.type
		,count(*) pizza_count_1yr
		,sum(o.retail_price)::numeric(8,2) gross_sales_1yr
		,(sum(o.retail_price)/p.total_resident_18yr_and_older)::decimal(6,4) gross_sales_per_capita_1yr
		,count(distinct x.customer_id) count_dist_cust_1yr
		,row_number() over (partition by c.state,o.type)
		from {{ params.ip_schema }}.stg_orders o
		inner join {{ params.ip_schema }}.stg_customer c
			on o.customer_id = c.customer_id
		inner join {{ params.ip_schema }}.census_adult_pop_by_state p
			on c.state = p.state_abbr
		left join cust_ordr_itm_more_than_once x
			on c.state = x.state and o.type = x.type
		group by c.state,o.type,p.total_resident_18yr_and_older
	)
, top_3_sel as (
	select *
	, dense_rank() over (partition by state order by gross_sales_1yr desc) rn
	from main
)
INSERT INTO {{ params.op_schema }}.top_sellers_by_state
select state, type, pizza_count_1yr, gross_sales_1yr, gross_sales_per_capita_1yr, count_dist_cust_1yr, rn as rank
, (current_timestamp(0) at time zone 'utc') as load_ts
from top_3_sel
where rn <=3
order by state asc, rn asc;
