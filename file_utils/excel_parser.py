from openpyxl import load_workbook

file_name = 'excel_file.xlsx'
wb = load_workbook(filename=file_name)

# workbook is always created with one worksheet.
ws = wb.active

for row in ws.rows:
    print row[0].value