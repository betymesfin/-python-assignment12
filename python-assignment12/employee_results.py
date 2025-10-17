import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with  sqlite3.connect("./db/lesson.db") as conn:  
    sql_statement = """SELECT last_name, SUM(price * quantity) AS revenue 
        FROM employees e 
        JOIN orders o ON e.employee_id = o.employee_id 
        JOIN line_items l ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id 
        GROUP BY e.employee_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())


df.plot(x="last_name", y="revenue", kind="bar", color="blue", title="Revenue per person")
plt.show()