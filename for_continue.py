numlist = [1, 2, 3, 'x', 4, 5]
sum = 0
for num in numlist :
    if not isinstance(num, (int, float)) :
        print(num, 'no int or float')
        continue
    sum += num
    print('num', '/', sum)