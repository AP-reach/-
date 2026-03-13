# Write your MySQL query statement below
with t
as(
    select * from Stadium
    where people >= 100
)

select s.id as id , s.visit_date as visit_date , s.people as people
from t s
where exists
(
    select 1
from t as s1 join t as s2 on s2.id = s1.id + 1 
join t as s3 on s3.id = s1.id +2 
where s.id in (s1.id , s2.id , s3.id)

)
order by s.id


