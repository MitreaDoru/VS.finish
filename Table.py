tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)
    for x in range(len(table[0])) :
        for y in range(len(table)) :
            print(table[y][x].rjust(colWidths[y]), end = ' ')
        print()
        x += 1

printTable(tableData)