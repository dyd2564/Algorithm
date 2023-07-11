-- 코드를 입력하세요
# SELECT author_id, author_name, category, total_sales

select d.author_id, c.author_name, d.category, d.total_sales  as total_sales
from author c join
(
select a.author_id, a.category, sum(b.sales*a.price) as total_sales
from book a join book_sales b
on a.book_id = b.book_id
where sales_date like '2022-01%'
group by 1,2
) d
on c.author_id = d.author_id
order by 1, 3 desc
