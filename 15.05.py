import os, PyPDF2
for folderName, subfolders, filenames in os.walk('D:\git-one'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        if filename.endswith('pdf'):
            pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
            if pdfReader.isEncrypted == True:
                pdfReader.decrypt('swordfish')
                pdfWriter = PyPDF2.PdfFileWriter()
                try:
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                        resultPdf = open('Decrypted'+filename, 'wb')
                        pdfWriter.write(resultPdf)
                        resultPdf.close()
                except PyPDF2.utils.PdfReadError:
                    print('The password for '+ filename + ' is incorrect!')
exit(0)