import pandas as pd

sales = pd.read_csv("../sales_data_2023.csv")
sales['Sale_Date'] = pd.to_datetime(sales['Sale_Date'])
sales['Month'] = sales['Sale_Date'].dt.to_period('M')
group_sales = sales.groupby(['Month','Geography'])['Sale_Amount'].sum()
print(group_sales)

group_sales.to_csv("../sales_metrics_by_region.csv")
