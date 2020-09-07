
--- recently working on sql 

with test as (
    select * from uds_test
)
select  t.name,t.age,t.number,t.all_score/t.num
from test t