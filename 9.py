import os, re, shelve
from pathlib import Path
File = open('C:\delicious\walnut\waffles\libs.txt')
contentFile = File.read()
RegexForVBN = re.compile(r'ADJECTIVE|VERB|ADVERB|NOUN')
VBN = RegexForVBN.findall(contentFile)
Text = ''
print(contentFile)
Text = Text + contentFile
for i in VBN:
    if i == 'ADJECTIVE':
        print('Enter an adjective:')
        Input = input('')
    elif i == 'VERB':
        print('Enter a verb:')
        Input = input('')
    elif i == 'ADVERB':
        print('Enter an adverb:')
        Input = input('')
    elif i == 'NOUN':
        print('Enter an NOUN:')
        Input = input('')
    Text = Text.replace(i, Input)
print(Text)
File.close()
File1 = open("C:\delicious\walnut\waffles\libsaf.txt", "w")
File1.write(Text)
File1.close()