spam = ['appels', 'bananas', 'tofu', 'cats']
spam[-1] = 'and ' + spam[-1]
New_list = ""
for name in spam:
    New_list = New_list + name + ', '
New_list = "'" + New_list +"'"
print(New_list)

