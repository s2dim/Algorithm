# Write your MySQL query statement below

with t as (
    select *, lag(amount) over(order by visited_on) as le1,
              lag(amount, 2) over(order by visited_on) as le2,
              lag(amount, 3) over(order by visited_on) as le3,
              lag(amount, 4) over(order by visited_on) as le4,
              lag(amount, 5) over(order by visited_on) as le5,
              lag(amount, 6) over(order by visited_on) as le6
    from (select visited_on, sum(amount) as amount
          from customer
          group by visited_on) as s
)

select visited_on, (amount + le1 + le2 + le3 + le4 + le5 + le6) as amount, round((amount + le1 + le2 + le3 + le4 + le5 + le6) / 7, 2) as average_amount
from t
where le1 is not null and
      le2 is not null and
      le3 is not null and
      le4 is not null and
      le5 is not null and
      le6 is not null
