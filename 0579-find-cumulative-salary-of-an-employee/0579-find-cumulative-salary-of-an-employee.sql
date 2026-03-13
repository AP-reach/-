# Write your MySQL query statement below
select Id, AccMonth as Month, sum(Salary) as Salary
from
(
    select a.Id as Id, a.Month as AccMonth, b.Month as Month, b.Salary as Salary
    from 
    (
        select Employee.Id as Id, Employee.Month as Month
        from Employee, (select Id, max(Month) as Month
            from Employee
            group by Id) as LastMonth
            where Employee.Id = LastMonth.Id and Employee.Month != LastMonth.Month) as a 
    join Employee as b
    on a.Id = b.Id and a.Month - b.Month <= 2 and a.Month - b.Month >= 0
) as acc
group by Id, AccMonth
order by Id, Month desc

