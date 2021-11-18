import random 

couple_married = []

list_of_boys=['f','g','h','i','j','k','l']
list_of_girls=['a','b','c','d','e']

count = len(list_of_girls)

for i in range(count):

    couple1 = random.choice(list_of_girls)
    couple2 = random.choice(list_of_boys)

    list_of_girls.remove(couple1)
    list_of_boys.remove(couple2)

    couple = [couple1,couple2]

    couple_married.append(couple)


print(couple_married)