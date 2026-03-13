# Write your MySQL query statement below
select t.id , t.company , t.salary 
from (
    select * , row_number()over(partition by company order by salary) as rn , count(*)over(partition by company) cn 
from Employee
) t
where 
    (t.cn % 2 = 1 AND t.rn = (t.cn + 1) / 2)
   OR (t.cn % 2 = 0 AND t.rn IN (t.cn / 2, t.cn / 2 + 1));

