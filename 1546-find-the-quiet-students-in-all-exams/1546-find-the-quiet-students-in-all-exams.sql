# Write your MySQL query statement below
with t as (
    select  student_id  ,  rank()over(partition by exam_id order by score) as rn1 , rank()over(partition by exam_id order by score desc) as rn2 
from Exam 
)

select s1.student_id , s1.student_name
from Student s1 join (
    select t.student_id , min(t.rn1) as rn1 , min(t.rn2) as rn2
from  t 
group by t.student_id
) s2 on s1.student_id = s2.student_id
where s2.rn1 != 1 and s2.rn2 != 1
order by s1.student_id
