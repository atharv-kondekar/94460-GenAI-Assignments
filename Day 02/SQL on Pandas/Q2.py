import pandas as pd
import pandasql as ps

data = pd.read_csv("books_hdr.csv")
print(data.dtypes)

query = """
SELECT id,name,author 
FROM books_hdr
WHERE price >=200
"""

result = ps.sqldf(query, {"books_hdr" : data})

print(result)