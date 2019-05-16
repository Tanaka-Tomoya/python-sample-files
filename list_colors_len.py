pos = int(input('select number:'))
colors = ['blue', 'red', 'green', 'yellow']
length = len(colors)
if -length <= pos < length :
    item = colors[pos]
    print(item)
else :
    print('error')