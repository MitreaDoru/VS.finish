import openpyxl, sys, os
wb = openpyxl.Workbook()
sheet = wb['Sheet']
x = 0
y = 0
for filename in os.listdir('D:\git-one'):
    
    if filename.endswith('.txt'):
        y += 1
        x = 0
        f = open(filename, 'r')
        for lines in f.readlines():
            x += 1
            sheet.cell(row=x, column=y).value = lines


wb.save('13dot1.xlsx')
sys.exit(0)