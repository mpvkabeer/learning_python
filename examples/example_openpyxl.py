import openpyxl as xl
wb = xl.load_workbook('datasets/sample_data_large.xlsx')
sheet = wb['data']
cell = sheet['a1'] # or cell = sheet.cell(1,1)
print(cell.value)
