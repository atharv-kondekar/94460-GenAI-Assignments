import pandas as pd
import pandasql as ps

emp_data = pd.read_csv("emp_hdr.csv")

query = """SELECT empno,ename 
FROM emp_hdr 
WHERE sal>=1000
"""
result = ps.sqldf(query , {"emp_hdr":emp_data} )

print(result)