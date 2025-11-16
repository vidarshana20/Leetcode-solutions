# Write your MySQL query statement below


select e.name, b.bonus from Employee e left join bonus b on e.empId=b.empId where b.bonus<1000 or b.bonus is null;


-- select 
--     e.name, b.bonus 
-- from 
--     Employee e 
--  join 
--     bonus b 
-- on 
--     e.empId=b.empId and b.bonus<1000;


