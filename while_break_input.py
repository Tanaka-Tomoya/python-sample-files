from random import randint

miss = 0
correct = 0
print('if you want to quit, press q')

while miss < 3 :
    a = randint(1, 100)
    b = randint(1, 100)
    ans = a + b
    question = f"what is {a} + {b}"
    value = input(question)

    if value == 'q' :
        break
    if value == str(ans) :
        correct += 1
        print('correct!')
    else :
        miss += 1
        print('fail', 'x' * miss)

print('-' * 20)
print('correct:', correct)
print('fail:', miss)