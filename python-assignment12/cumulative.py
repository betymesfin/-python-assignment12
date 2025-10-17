import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

with  sqlite3.connect("./db/lesson.db") as conn:
    query = """
        SELECT o.order_id,SUM(li.quantity * p.price) AS total_price
        FROM orders o
        JOIN line_items li ON o.order_id = li.order_id
        JOIN products p ON li.product_id = p.product_id
        GROUP BY o.order_id
        ORDER BY o.order_id;
        """
df = pd.read_sql_query(query, conn)
print(df.head())

def cumulative(row):
    totals_above = df['total_price'][0:row.name + 1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

df.plot(
    x='order_id',
    y='cumulative',
    kind='line',
    title='Cumulative Revenue by Order ID',
)
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.show()