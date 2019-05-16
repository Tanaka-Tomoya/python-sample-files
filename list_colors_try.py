pos = int(input('select number:'))
colors = ['blue', 'red', 'green', 'yellow']
length = len(colors)
try :
    item = colors[pos]
    print(item)
except IndexError :
    print('index error')
except Exception as error :
    print(error)
