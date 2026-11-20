# Write your MySQL query statement belows
select activity_date as day, count(user_id) as active_users
from (select distinct user_id, activity_date
        from activity
        where activity_date between '2019-06-28' and '2019-07-27') t
group by activity_date