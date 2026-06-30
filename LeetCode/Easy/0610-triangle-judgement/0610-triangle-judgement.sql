# Write your MySQL query statement below
select x, y, z, (case
    when greatest(x, y, z) < x + y + z - greatest(x, y, z) then "Yes"
    else "No"
    end) as triangle
from triangle
