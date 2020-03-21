#Excel can save a spreadsheet to a CSV file with a few mouse clicks, but if you had to convert hundreds of Excel files to CSVs, it would take hours of clicking. 
#Using the openpyxl module from Chapter 12, write a program that reads all the Excel files in the current working directory and outputs them as CSV files.
#A single Excel file might contain multiple sheets; you’ll have to create one CSV file per sheet. 
#The filenames of the CSV files should be <excel filename>_<sheet title>.csv, where <excel filename> is the filename of the Excel file without the file extension (for example, 'spam_data', not 'spam_data.xlsx') and <sheet title> is the string from the Worksheet object’s title variable.
import os, openpyxl, csv
for excelFile in os.listdir('D:\PDF-uri'):
    if excelFile.endswith('.xlsx'):
        name = os.path.splitext(excelFile)[0]
        wb = openpyxl.load_workbook(excelFile)
        for sheetName in wb.get_sheet_names():
            sheet = wb.get_sheet_by_name(sheetName)   
            f = open(name +'__' + sheetName + '.csv', 'w', newline='')
            outputWriter = csv.writer(f)
            for rowNum in range(1, sheet.max_row + 1):
                rowData = []   
                for colNum in range(1, sheet.max_column + 1): 
                    rowData.append(sheet.cell(row=rowNum, column=colNum).value)
                outputWriter.writerow(rowData)
                
        f.close()

