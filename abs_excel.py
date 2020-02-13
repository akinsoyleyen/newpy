import openpyxl
import os
#import os ; python calistigi directory i degistirebilmek icin import edilir....

os.chdir('/Users/akin/onedrive/python3/documents')

#burada detay yazmamiza gerek yok cunku zaten directory yi belirttik ustte
workbook = openpyxl.load_workbook('example.xlsx')

#Bu sekilde o kiptalikta istedigimiz sheet e gidiyoruz.
sheet = workbook.get_sheet_by_name('Sheet1')

#Bu sekilde o sheet teki Cell e gidiyoruz
cell = sheet['A1']

#Bunun icin bir loop yaparsak
for i in range(1, 8):
    print(i, sheet.cell(row=i, column=2).value)
