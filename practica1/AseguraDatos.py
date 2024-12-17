import pandas as pd
from datetime import datetime
sales = pd.read_csv('sales_data_2023.csv')
#Eliminar valores duplicados
csvSinDuplicados = sales.drop_duplicates()
print(csvSinDuplicados.head())
#Verifica que Sales amount sea de tipo númerico, en caso contrario cambia el valor
csvSinDuplicados['Sale_Amount'] = csvSinDuplicados['Sale_Amount'].astype('float64')
print(csvSinDuplicados.dtypes)

#Revisa si las fechas contienen el formato correcto en dd/mm/YYYY
saleDate = sales.iloc[:5, 3]
formatDateTime = "%Y-%m-%d"
try:
    for dates in saleDate:
        datetime.strptime(dates, formatDateTime)
except Exception as ex:
    print('¡¡¡¡¡¡ Hay fechas invalidas !!!!!!!')
