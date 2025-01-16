import pandas as pd

sales_data = pd.read_csv("../sales_data_2023.csv")

def Avarage_Sales(sales):
    sum_sales = sum(sales)
    total_data = len(sales)
    avarege = sum_sales / total_data
    return avarege

def Max_Sales(sales):
    return sales.max()

def Min_Sales(sales):
    return sales.min()


print("Avarage Sales: ")
print(Avarage_Sales(sales_data["Sale_Amount"]))

print("Sale MAX: ")
print(Max_Sales(sales_data["Sale_Amount"]))

print("Sale Min:")
print(Min_Sales(sales_data["Sale_Amount"]))