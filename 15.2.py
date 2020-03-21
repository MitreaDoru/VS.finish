import PyPDF2
f = open('dictionary.txt')
pdfReader = PyPDF2.PdfFileReader(open('encryptedmeetingminutes2.pdf', 'rb'))
for word in f:
    print(word)
    word = word.rstrip()
    if pdfReader.decrypt(word) == 1:  
        print('The password is ' + word)
        break
    elif pdfReader.decrypt(word.lower()) == 1:
        print('The password is ' + word.lower())
        break
exit(0)


    

