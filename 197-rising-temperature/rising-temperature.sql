select 
    w2.id 
from 
    Weather w1 
left join 
Weather w2 
on 
w1.recordDate = DATE_SUB(w2.recordDate, INTERVAL 1 DAY)
where w1.temperature<w2.temperature