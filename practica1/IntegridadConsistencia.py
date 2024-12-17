import pandas as pd
from datetime import datetime
customers = pd.read_csv('customer_data_2023.csv')
sales = pd.read_csv('sales_data_2023.csv')
##### VALIDACIÓN DE DATOS DE customer_data_2023.csv #####
print('##### VALIDACIÓN DE DATOS DE customer_data_2023.csv #####')

#Tipos de datos en cada columna
print(customers.dtypes)

#Valida tipo de datos apropiados para cada  columna
try:
    pd.to_numeric(customers['Customer_ID'], errors='raise')
    print('Customer_ID contiene datos validos')
except Exception as ex:
    print('Customer_ID no contiene datos invalidos')


try:
    pd.to_numeric(customers['Customer_Name'], errors='raise')
    print('Customer_Name contiene datos invalidos')
except Exception as ex:
    print('Customer_Name contiene datos validos')
    
try:
    pd.to_numeric(customers['Customer_Age'], errors='raise')
    print('Customer_Age contiene datos validos')
except Exception as ex:
    print('Customer_Age no contiene datos invalidos')

try:
    pd.to_numeric(customers['Geography'], errors='raise')
    print('Geography contiene datos invalidos')
except Exception as ex:
    print('Geography no contiene datos validos')


print('##### VALIDACIÓN DE DATOS DE customer_data_2023.csv #####')
#VALIDA QUE NO HAYA VALORES NULOS
print('Total de valores nulos en cada columna')

print(customers.isnull().sum())


print('##### VALIDACIÓN DE DATOS DE sales_data_2023.csv #####')

#Tipos de datos en cada columna
print(sales.dtypes)

#Valida tipo de datos apropiados para cada  columna
try:
    pd.to_numeric(sales['Sale_ID'], errors='raise')
    print('Sale_ID contiene datos validos')
except Exception as ex:
    print('Sale_ID no contiene datos invalidos')
    
try:
    pd.to_numeric(sales['Customer_ID'], errors='raise')
    print('Customer_ID contiene datos validos')
except Exception as ex:
    print('Customer_ID no contiene datos invalidos')
    
try:
    pd.to_numeric(sales['Sale_Amount'], errors='raise')
    print('Sale_Amount contiene datos validos')
except Exception as ex:
    print('Sale_Amount no contiene datos invalidos')

saleDate = sales.iloc[:5, 3]
formatDateTime = "%d-%m-%Y"
try:
    for dates in saleDate:
        datetime.strptime(dates, formatDateTime)
    print('Sale_Date contiene datos validos')
except Exception as ex:
    print('Sale_Date contiene datos invalidos')

try:
    pd.to_numeric(sales['Geography'], errors='raise')
    print('Geography contiene datos invalidos')
except Exception as ex:
    print('Geography contiene datos validos')
    


#VALIDA QUE NO HAYA VALORES NULOS
print('Total de valores nulos en cada columna')
print(sales.isnull().sum())