#   Created by Elshad Karimov on 10/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Accessing/Traversing the list
import numpy

# data need not be of same type in a list
# ex: [1, 's', {x: 1}]

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")


# Update/Insert - List

myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
myList.insert(4, 15)

myList.append(55)

newList = [11, 12, 13, 14]
myList.extend(newList)
print(myList)

del myList[0]
myList.remove[12]  # remves first occurence

avg = round(sum(myList)/len(myList), 2)


#  Searching for an element in the List
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def lin_serch():
    for i, val in enumerate(myList):
        if val == 10:
            return 1
    return -1


def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'


print(searchinList(myList, 100))


#  List operations / functions

a = [0, 1] * 4
# [0, 1, 0, 1, 0, 1, 0, 1]
len(a)
max(a)
min(a)
sum(a)
total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    average = total / count

print('Average:', average)


numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

# Strings
a = 'spkknn'
b = list(a)

a = 'sdd-sss-sfdf'
b = a.split('-')
'-'.join(b)

# sort
newList = [34, 12, 15, 14]
newList.sort()
newList = newList + [344]

# copy list
orig = newList[:]

#
# Array good for arithmetics operations
a = numpy.array(newList)


# List can have differet datatypes

# List comprehensio
new_list = [i*2 for i in newList]

# conditional
new_list = [i*2 for i in newList if i != 0]


def is_consonnat(l):
    return True


s = 'srihari'
new_list = [l for l in s if is_consonnat(i)]

new_list = [i*2 if i > 0 else i*3 for i in newList if i != 0]


def get_n(i):
    return i


new_list = [get_n(i) for i in newList if i != 0]
