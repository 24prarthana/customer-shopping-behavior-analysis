select * from customer
limit 20

--------total revenue by male and female---------
select gender, SUM(purchase_a) as revenue
from customer 
group by Gender

drop database customer shopping behavior