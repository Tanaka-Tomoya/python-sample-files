numlist = [3, 4, 5, 88765, 8 ,9]
sum = 0
for num in numlist :
    if not isinstance(num, (int, float)) :
        print(num, 'not int or float')
        break
    sum += num
else :
    print('total', sum)