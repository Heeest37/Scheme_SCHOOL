import pandas as pd
import datetime

xls = pd.ExcelFile(r"C:/Users/User/PycharmProjects/PyQTMAPS/Книга1.xlsx") # use r before absolute file path

now = datetime.datetime.now()

sheetX = xls.parse(0) #2 is the sheet number+1 thus if the file has only 1 sheet write 0 in paranthesis

var1 = sheetX[now.strftime("%A")]

print(var1[0])