import ezsheets, openpyxl
ss = ezsheets.Spreadsheet('1a3ZNbUijLIJ15awW93-51OC92pepAEwOeld1VddoRFA')
sheet = ss.sheets
ss.downloadAsExcel('email.xlsx')
wb = openpyxl.load_workbook('email.xlsx')
sheet1 = wb.active
sheet1 = wb['Form Responses 1']
f = open('Coloana.txt', 'w+')
for x in range(2,sheet1.max_row+1):
    f.write(sheet1.cell(row=x, column=3).value+'\n')
f.close()