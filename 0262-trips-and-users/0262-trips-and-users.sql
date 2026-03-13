select s1.request_at as 'Day' , 
round(
    sum(s1.status <> 'completed') / count(*) ,
    2
) as 'Cancellation Rate'
from Trips as s1 join
Users as s2 on s1.client_id = s2.users_id and s2.banned = 'No' join
Users as s3 on s1.driver_id = s3.users_id and s3.banned = 'No' 
where s1.request_at between '2013-10-01' and '2013-10-03'
group by s1.request_at 

