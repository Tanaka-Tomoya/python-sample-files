sum = 7600
while True:
    num = input('How many people')
    if num == 'q':
        print('exit')
        break
    try:
        price = round(sum / int(num))
    except Exception as error :
        print('error')
        print(error)
    else :
        if price < 0 :
          continue
        print(price)
