# Write your MySQL query statement below
select s1.Score,count(distinct(s2.score)) 'Rank' 
from Scores s1 join Scores s2 
on s1.score<=s2.score 
group by s1.Id 
order by s1.Score desc;