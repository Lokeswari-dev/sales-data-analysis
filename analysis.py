import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/Superstore.csv",encoding="latin1")
print(df.head())
print("\nShape:")
print(df.shape)
print("\nColumns:")
print(df.columns)
print("\nInfo:")
print(df.info())
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Ship Date']=pd.to_datetime(df['Ship Date'])
print(df[['Order Date', 'Ship Date']].dtypes)
print("\nDuplicate rows:",df.duplicated().sum())
#1.Total Sales & Total Profit
total_sales=df['Sales'].sum()
total_profit=df['Profit'].sum()
print("Total Sales:", total_sales)
print("Total Profit:",total_profit)

#2.Average order value
avg_sales = df['Sales'].mean()
print("Average Sales:", avg_sales)

#3.Category-wise Sales
category_sales=df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nCategory-wise Sales:")
print(category_sales)

#4. Top 5 Sub-Categories by profit
top_subcat_profit=df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 sub-Categories by Profit:")
print(top_subcat_profit)

#Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

#Loss making Analasys
loss_subcat = df.groupby('Sub-Category')['Profit'].sum().sort_values()
print("\nLoss making Sub-Categories:")
print(loss_subcat.head(5))

# Convert Period to string for plotting
monthly_sales_plot = monthly_sales.copy()
monthly_sales_plot.index = monthly_sales_plot.index.astype(str)

plt.figure()
plt.plot(monthly_sales_plot.values)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.show()

