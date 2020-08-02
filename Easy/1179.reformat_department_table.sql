# Write your MySQL query statement below
SELECT
    id,
    sum( if( month = 'Jan', revenue, null ) ) AS Jan_Revenue,  #if month is 'Jan', then revenue, else null.
    sum( if( month = 'Feb', revenue, null ) ) AS Feb_Revenue,  #sum is used because we need to get one row for each id we need to aggregate by id using GROUP BY. But since we have multiple rows with the same id but different values (e.g. for id=1 we have Jan_Revenues: NULL, 8000 and NULL. When we merge these 3 together what value should be chosen? This is why we need either SUM (NULL+8000+NULL) or MAX, in both cases 8000 will be used.
    sum( if( month = 'Mar', revenue, null ) ) AS Mar_Revenue,
    sum( if( month = 'Apr', revenue, null ) ) AS Apr_Revenue,
    sum( if( month = 'May', revenue, null ) ) AS May_Revenue,
    sum( if( month = 'Jun', revenue, null ) ) AS Jun_Revenue,
    sum( if( month = 'Jul', revenue, null ) ) AS Jul_Revenue,
    sum( if( month = 'Aug', revenue, null ) ) AS Aug_Revenue,
    sum( if( month = 'Sep', revenue, null ) ) AS Sep_Revenue,
    sum( if( month = 'Oct', revenue, null ) ) AS Oct_Revenue,
    sum( if( month = 'Nov', revenue, null ) ) AS Nov_Revenue,
    sum( if( month = 'Dec', revenue, null ) ) AS Dec_Revenue
FROM
    Department
GROUP BY
    id;
