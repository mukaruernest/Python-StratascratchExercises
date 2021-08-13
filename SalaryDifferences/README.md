## Exercise: Salaries Differences

## Table of Contents
- [DataSet](https://github.com/mukaruernest/StratascratchExercises/tree/master/SalaryDifference#dataset)
- [Question](https://github.com/mukaruernest/StratascratchExercises/tree/master/SalaryDifference#question)
- [Solution](https://github.com/mukaruernest/StratascratchExercises/tree/master/SalaryDifference#solution)
- [Result](https://github.com/mukaruernest/StratascratchExercises/tree/master/SalaryDifference#result)

More details about this exercise can be found on [Stratascratch website](https://platform.stratascratch.com/coding-question?id=10308&python=)

## DataSet

`db_employee`
`db_dept`

 

**Table Name: db_employee**

DataSet shows the first ten rows of the table, to view the full table follow [this link](https://platform.stratascratch.com/coding-question/output-preview) 

<details>
  <summary>Click to view table db_employee</summary>
<html><body>
<!--StartFragment-->

id | first_name | last_name | salary | department_id
-- | -- | -- | -- | --
10301 | Keith | Morgan | 27056 | 2
10302 | Tyler | Booth | 32199 | 3
10303 | Clifford | Nguyen | 32165 | 2
10304 | Mary | Jones | 49488 | 3
10305 | Melissa | Lucero | 27024 | 3
10306 | Ashley | Li | 28516 | 4
10307 | Joseph | Solomon | 19945 | 1
10308 | Anthony | Sanchez | 43801 | 3
10309 | Katherine | Huffman | 12984 | 4
10310 | Dawn | Foley | 28902 | 2
10311 | Melissa | Holmes | 33575 | 1

<!--EndFragment-->
</body>
</html>

</details>

**Table Name: db_dept**

<details>
  <summary>Click to view table db_dept</summary>
<html><body>
<!--StartFragment-->

id | department
-- | --
1 | engineering
2 | human resource
3 | operation
4 | marketing
5 | sales
6 | customer care

<!--EndFragment-->
</body>
</html>
</details>

## Question 

Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the difference in salaries.

## Solution

```Py
import pandas as pd
import numpy as np

df = pd.merge(db_employee, db_dept, how = 'left',left_on = ['department_id'], right_on=['id'])
df1=df[df["department"]=='engineering']
df_eng = df1.groupby('department')['salary'].max().reset_index(name='eng_salary')
df2=df[df["department"]=='marketing']
df_mkt = df2.groupby('department')['salary'].max().reset_index(name='mkt_salary')
result = pd.DataFrame(df_mkt['mkt_salary'] - df_eng['eng_salary'])
result.columns = ['salary_difference']
result
```

## Result
| salary_difference |
|-------------------|
| 2400              |
