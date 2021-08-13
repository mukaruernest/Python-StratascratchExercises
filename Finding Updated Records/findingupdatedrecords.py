import pandas as pd

df = ms_employee_salary.groupby(['id','first_name','last_name','department_id'])['salary'].max().reset_index()

