import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales_data_2023.csv')
# print(sales.head())
salesByGeography = sales.groupby('Geography')['Sale_Amount'].sum().reset_index()
print('Reporte de ventas por área')
print(salesByGeography)
plt.bar(salesByGeography['Geography'], salesByGeography['Sale_Amount'])
plt.xlabel('Región')
plt.ylabel('Total de vendido')