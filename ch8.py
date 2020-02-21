import pyinputplus as pyip
cost = 0
print('What bread type you want?')
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
if bread == 'wheat':
    cost += 2
elif bread == 'white':
    cost += 1
elif bread == 'sourdough':
    cost += 3
print('What protein type you want?')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
if protein == 'chicken':
    cost += 5
elif protein == 'turkey':
    cost += 5
elif protein == 'ham':
    cost += 4
elif protein == 'tofu':
    cost += 3
cheeseAsk = pyip.inputYesNo(prompt='You want cheese?')
while cheeseAsk == 'yes':
    print('What cheese type you want')
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
    if cheese == 'cheddar':
        cost += 3
    elif cheese == 'swiss':
        cost += 4
    elif cheese == 'mozzarella':
        cost += 3
    break
sosAsk = pyip.inputYesNo(prompt='You want mayo, mustard, lettuce or tomato?')
while sosAsk == 'yes':
    print('What sos you want')
    sos = pyip.inputMenu(['mayo', 'mustrad', 'lettuce', 'tomato'])
    if sos == 'mayo':
        cost += 2
    elif sos == 'mustrad':
        cost += 1
    elif sos == 'lettuce':
        cost += 2
    elif sos == 'tomato':
        cost += 1
    break
print('You want 1 sandwiche?')
howmany = pyip.inputNum(greaterThan=0)
cost = cost * howmany
print(cost)
