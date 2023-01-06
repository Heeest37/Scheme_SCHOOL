import pandas as pd
import datetime

xls = pd.ExcelFile(r"C:/Users/User/PycharmProjects/PyQTMAPS/Книга1.xlsx")

now = datetime.datetime.now()

sheetX = xls.parse(0)

var1 = sheetX[now.strftime("%A")]

print(var1[0])