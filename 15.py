import os, PyPDF2
for folderName, subfolders, filenames in os.walk('D:\PDF-uri'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        if filename.endswith('pdf'):
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()

            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt('swordfish')
                resultPdf = open('encrypted'+filename, 'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()
            pdfReader = PyPDF2.PdfFileReader(open('encrypted'+filename, 'rb'))
            pdfReader.decrypt('swordfish')
            try:
                pageObj = pdfReader.getPage(0)
            except PyPDF2.utils.PdfReadError:
                print('The password is wrong.')
            else:
                print('Files encrypted correct')
exit(0)
