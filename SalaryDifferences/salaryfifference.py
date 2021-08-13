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
