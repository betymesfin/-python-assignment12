import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))

df['strength'] = df['strength'].astype(str).str.replace(r'[^0-9.]', '', regex=True)

df['strength'] = df['strength'].astype(float)
print(df.dtypes)


fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
)
fig.write_html("wind.html", auto_open=True)