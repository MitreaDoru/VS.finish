import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss.sheets
for x in range(2,15001):
    if int(ss[0].getRow(x)[0]) * int(ss[0].getRow(x)[1]) != int(ss[0].getRow(x)[2]):
        print('Row' + str(x) + 'has incorrect total')
