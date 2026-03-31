select
	column1
,	column2
,	column3
from
	schema.table_name alias
join
	schema.table_name alias2 on alias.column1 = alias2.column1 and alias.column2 = alias2.column1
where
	alias.column1 = 'value'
group by
	column1
,	column2
,	column3
order by
	column1
,	column2