import ezsheets
ss = ezsheets.Spreadsheet('1a3ZNbUijLIJ15awW93-51OC92pepAEwOeld1VddoRFA')
sheet = ss.sheets
ss.downloadAsExcel('email.xlsx')
ss.downloadAsODS('email1.ods')
ss.downloadAsCSV('email2.csv')
ss.downloadAsTSV('email3.tsv')
ss.downloadAsPDF('email4.pdf')
ss.downloadAsHTML('email5.html')