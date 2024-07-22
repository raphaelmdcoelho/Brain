A ***window function*** performs a calculation across a set of table rows that are somehow related to the current row.

This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities.


```sql
SELECT duration_seconds, 
	   SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total 
FROM tutorial.dc_bikeshare_q1_2012
```

The first part of the above aggregation, `SUM(duration_seconds)`, looks a lot like any other aggregation. Adding `OVER` designates it as a window function. You could read the above aggregation as "take the sum of `duration_seconds` _over_ the entire result set, in order by `start_time`."

```sql
SELECT start_terminal, 
	   duration_seconds, 
	   SUM(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time) AS running_total 
FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08'
```

```sql
SELECT start_terminal, 
	   duration_seconds, 
	   SUM(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time) AS running_total, 
	   COUNT(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time) AS running_count, 
	   AVG(duration_seconds) OVER (PARTITION BY start_terminal ORDER BY start_time) AS running_avg 
FROM tutorial.dc_bikeshare_q1_2012 
WHERE start_time < '2012-01-08'
```

```sql
SELECT start_terminal, start_time, duration_seconds, ROW_NUMBER() OVER (ORDER BY start_time) AS row_number FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08'
```

```sql
SELECT start_terminal, start_time, duration_seconds, ROW_NUMBER() OVER (PARTITION BY start_terminal ORDER BY start_time) AS row_number FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08'
```

You can use window functions to identify what percentile (or quartile, or any other subdivision) a given row falls into. The syntax is `NTILE(*# of buckets*)`. In this case, `ORDER BY` determines which column to use to determine the quartiles (or whatever number of 'tiles you specify). For example:

```sql
SELECT start_terminal, duration_seconds, NTILE(4) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS quartile, NTILE(5) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS quintile, NTILE(100) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS percentile FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08' ORDER BY start_terminal, duration_seconds
```

## LAG and LEAD

It can often be useful to compare rows to preceding or following rows, especially if you've got the data in an order that makes sense. You can use `LAG` or `LEAD` to create columns that pull values from other rows—all you need to do is enter which column to pull from and how many rows away you'd like to do the pull. `LAG` pulls from previous rows and `LEAD` pulls from following rows:

```sql
SELECT start_terminal, duration_seconds, LAG(duration_seconds, 1) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS lag, LEAD(duration_seconds, 1) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS lead FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08' ORDER BY start_terminal, duration_seconds
```

This is especially useful if you want to calculate differences between rows:

```sql
SELECT start_terminal, duration_seconds, duration_seconds -LAG(duration_seconds, 1) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS difference FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08' ORDER BY start_terminal, duration_seconds
```

The first row of the `difference` column is null because there is no previous row from which to pull. Similarly, using `LEAD` will create nulls at the end of the dataset. If you'd like to make the results a bit cleaner, you can wrap it in an outer query to remove nulls:

```sql
SELECT * FROM ( SELECT start_terminal, duration_seconds, duration_seconds -LAG(duration_seconds, 1) OVER (PARTITION BY start_terminal ORDER BY duration_seconds) AS difference FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08' ORDER BY start_terminal, duration_seconds ) sub WHERE sub.difference IS NOT NULL
```

## Windows Alias

```sql
SELECT start_terminal, duration_seconds, NTILE(4) OVER ntile_window AS quartile, NTILE(5) OVER ntile_window AS quintile, NTILE(100) OVER ntile_window AS percentile FROM tutorial.dc_bikeshare_q1_2012 WHERE start_time < '2012-01-08' WINDOW ntile_window AS (PARTITION BY start_terminal ORDER BY duration_seconds) ORDER BY start_terminal, duration_seconds
```

#database #sqlserver 