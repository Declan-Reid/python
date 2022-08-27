from random import randint
from simpleeval import simple_eval

brackets = randint(0, 1)

sign = {
    1: randint(1, 4),
    2: randint(1, 4),
    3: randint(1, 4),
    4: randint(1, 4)
}

for i in range(4):
    if sign[i+1] == 1:
        sign[i+1] = '+'
    if sign[i+1] == 2:
        sign[i+1] = '-'
    if sign[i+1] == 3:
        sign[i+1] = '*'
    if sign[i+1] == 4:
        sign[i+1] = '/'

if brackets == 0:
    equation = str(randint(1, 30))+sign[1]+str(randint(1, 30))+sign[2]+'('+str(randint(1, 30))+sign[3]+str(randint(1, 30))+')'+sign[4]+str(randint(1, 30))
else:
    equation = str(randint(1, 30))+sign[1]+str(randint(1, 30))+sign[2]+str(randint(1, 30))+sign[3]+str(randint(1, 30))+sign[4]+str(randint(1, 30))


print('Your equation is: '+equation.replace('*', 'x').replace('/', '÷'))
print('The answer is: '+str(float(simple_eval(equation))))