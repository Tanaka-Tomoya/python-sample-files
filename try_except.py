while True:
    num = input('How many')
    if num == 'q' :
        print('exit')
        break
    try:
        price = 120 * int(num)
        print('total', price)
    except:
        print('error')
