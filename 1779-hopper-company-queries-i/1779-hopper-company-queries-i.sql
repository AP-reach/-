# Write your MySQL query statement below
with recursive temp as (
    select 1 as n
    union all
    select n + 1
    from temp
    where n + 1 <= 12
),
accepted as(
    select s1.ride_id , month(s1.requested_at) as req_month
    from Rides s1 join AcceptedRides s2 on s1.ride_id = s2.ride_id
    where year(s1.requested_at) = 2020 
),
tab1 as(
    select s.n , if(s1.driver_id is null, 0 , count(s1.driver_id)) as active_drivers
from temp s left join Drivers s1 on year(s1.join_date) < 2020 or (year(s1.join_date) = 2020 and month(s1.join_date) <= s.n) 
group by s.n
),
tab2 as(
    select t.n  , if(s2.ride_id is null,0 ,count(s2.ride_id)) as accepted_rides
from temp t left join accepted s2 on 
t.n = s2.req_month 
group by t.n 
)

select t1.n as 'month' , t1.active_drivers , t2.accepted_rides
from tab1 t1 join tab2 t2 on t1.n = t2.n
