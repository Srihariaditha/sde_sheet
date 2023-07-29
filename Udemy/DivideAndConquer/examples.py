from Udemy.DivideAndConquer.convertString import findMinOperation
from Udemy.DivideAndConquer.houseRobber import houseRobber
from Udemy.DivideAndConquer.findLCS import findLCS
from Udemy.DivideAndConquer.findLPS import findLPS
from Udemy.DivideAndConquer.zoKnapsack import zoKnapsack

# Merge Sort
################################


def merge(clist, l, m, h):
    n1 = m-l+1
    n2 = h-m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = clist[l+i]
    for i in range(n2):
        R[i] = clist[m+i+1]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            clist[k] = L[i]
            i = i+1
        else:
            clist[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        clist[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        clist[k] = R[j]
        j += 1
        k += 1


def mergeSort(clist, low, high):
    if low < high:
        m = (low + (high-1))//2
        mergeSort(clist, l, m)
        mergeSort(clist, m+1, high)
        merge(clist, low, m, high)
    return clist


l = [34, 56, 23, 67, 89, 12, 9, 6, 1, 100]
print(mergeSort(l, 0, len(l)-1))


# Quick sort
################################
def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            if i != j:
                customList[i], customList[j] = customList[j], customList[i]
    customList[i+1], customList[high] = customList[high], customList[i+1]
    return (i+1)


def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi-1)
        quickSort(customList, pi+1, high)


l = [34, 56, 23, 67, 89, 12, 9, 6, 1, 100]
quickSort(l, 0, len(l)-1)
print(l)

# Fibonacci
################################


def fibonacci(n):
    if n < 1:
        return 'error'
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(23))

# Factorial
################################


def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))
