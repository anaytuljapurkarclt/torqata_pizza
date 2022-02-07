create table if not exists {{ params.op_schema }}.top_sellers_by_state_archive
as select * from {{ params.op_schema }}.top_sellers_by_state where 1=0;
