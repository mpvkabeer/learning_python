import openpyxl as xl
wb = xl.load_workbook('sample_data_large.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1'] # or cell = sheet.cell(1,1)
print(cell,value)
