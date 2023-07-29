import numpy as np
import array

my_array = array.array('i', [1, 2, 3])
print(my_array)


twoDAray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twoDAray)

new2DAray = np.insert(twoDAray, 0, [1, 2, 4], axis=1)
print(new2DAray)


new3DAray = np.append(twoDAray, [1, 2, 4])
print(new3DAray)


def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
        # print()


traverse(twoDAray)


def search2DArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "Value at row " + str(i) + "col " + str(j)
    return "Not found"


print(search2DArray(twoDAray, 2))

x = np.delete(twoDAray, 0, axis=0)
print(x)
