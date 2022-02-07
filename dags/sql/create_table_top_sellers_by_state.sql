CREATE TABLE IF NOT EXISTS {{ params.op_schema }}.top_sellers_by_state
(
    state character(2) COLLATE pg_catalog."default",
    type character varying(20) COLLATE pg_catalog."default",
    pizza_count_1yr bigint,
    gross_sales_1yr numeric(8,2),
    gross_sales_per_capita_1yr numeric(6,4),
    count_dist_cust_1yr bigint,
    rank bigint,
	load_ts timestamp
);

create index on {{ params.op_schema }}.top_sellers_by_state (state);
create index on {{ params.op_schema }}.top_sellers_by_state (type);
