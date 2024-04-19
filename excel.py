import openpyx1

wb=openpyx1.Workbook()
sheet=wb.active

sheet['A1']="Amit"
sheet.cell(row=1,column=2,value="Deepak")

wb.save("/root/test.xlsx")
