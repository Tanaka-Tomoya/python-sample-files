numlist = [1, 2, 3, 'x']
sum = 0
for num in numlist :
    if not isinstance(num, (int, float)) :
        print(num, 'not int or float')
        break
    sum += num
    print(num, "/", sum)