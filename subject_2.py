import sqlite3
import pandas as pd

with sqlite3.connect('db.sqlite3') as conn:
     df= pd.read_sql_query("SELECT * from user", conn)


df['fulname'] = df['first_name'] + ' ' + df['last_name']

print(df)
df.to_excel("output.xlsx")
print()

print(df.mean())

print(df.std())

