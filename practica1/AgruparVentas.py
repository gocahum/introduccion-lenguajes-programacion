import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales_data_2023.csv')
print(sales.head())
salesByGeography = sales.groupby('Geography')['Sale_Amount'].sum().reset_index()
plt.bar(salesByGeography['Geography'], salesByGeography['Sale_Amount'])
plt.xlabel('Area de ventas')
plt.ylabel('Total de ventas')