#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

#  Missing Number

import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2

    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)

    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr

    return missing


#  Find Pairs
#  LeetCode 1 - Two Sum

def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)


myList = [1, 2, 3, 2, 3, 4, 5, 6]
find_pairs(myList, 6)

# Leetcode answer


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


# Find a number
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    12, 13, 14, 15, 16, 17, 18, 19, 20])


def find_number(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)


# Find max product of two integer

def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization

    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment

    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication


arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)

# findMaxProduct(myArray)


# Middle
def middle(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1]


my_list = [1, 2, 3, 4]

print(middle(my_list))  # Output: [2, 3]

# 2D List


def diagonal_sum(matrix):
    # Initialize the sum to 0
    total = 0

    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]

    return total

# Best Score


def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')

    for num in my_list:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num != max1:
            max2 = num

    return max1, max2


my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(my_list))  # Output: (90, 87)

# Duplicate Numbers


def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst


my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]

# Pairs


def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result


arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']

# Contains Duplicate


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicates(nums))  # Output: True


# Permutation

def permuntation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


# Rotate Matrix

def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row

#Max subarray 1D - Kadanes
oneDArray = [-11, -15, -10, 6]
def kadanes(A):
    sum=0
    ans = float('-inf')
    for v in A:
        sum = sum+v
        ans = max(sum, ans)
        if sum<0:
            sum=0
    return ans

# print(kadanes(oneDArray))


twoDArray = [[11, -15, -10, 6], [10, 14, -11, 5], [12, -17, 12, 8], [15, 18, 14, 9] ]

def getPrefixSumMatrix(A):
    rows, cols = (len(A), len(A[0]))
    pf = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        sum = 0
        for j in range(cols):
            sum = sum + A[i][j]
            pf[i][j] = sum
    for j in range(cols):
        sum = pf[0][j]
        for i in range(1, rows):
            sum = sum + pf[i][j]
            pf[i][j] = sum  
    return pf

def getPrefixColSumMatrix(A, rows):
    cols = len(A[rows])
    if rows==0:
        return A[0]
    pf = [A[0][i] for i in range(cols)] 
    for j in range(cols):
        sum = pf[j]
        for i in range(1, rows):
            sum = sum + pf[j]
            pf[j] = sum  
    return pf
        
def traverseTDArray(array):
    for i in range(len(array)):
        # for j in range(len(array[0])):
            print(array[i])     
   
# pf = getPrefixSumMatrix(twoDArray)
# traverseTDArray(pf)


def max_2d_sub_matrix_sum(A):
    row_len, col_len = len(A), len(A[0])
    ans = float('-inf')
    for i in range(row_len):
        for j in range(col_len):
            pf = getPrefixColSumMatrix(A,i)
            max_sum = kadanes(pf)
            ans = max(max_sum, ans)
    return ans

print(max_2d_sub_matrix_sum(twoDArray))

twoDArray = [[11, -15, -10, 6], [10, 14, -11, 5], [12, -17, 12, 8], [15, 18, 14, 9] ]

#contribution technique to get sum of all sub matrices
def max_2d_sum_all_sub_matrix_sum_ct(A):
    row_len, col_len = len(A), len(A[0])
    ans = 0
    for i in range(row_len):
        for j in range(col_len):
            tl = (i+1)*(j+1)
            br = (row_len-i)*(col_len-j)
            ct = tl * br * A[i][j]
            ans += ct
    return ans

print(max_2d_sub_matrix_sum_ct(twoDArray))

#Given a matrix every row is sorted and every col is sorted, find max sub matrix sum
#kadanes 2d willwork but other solution
#BR is always fixed here
def max_2d_max_sub_matrix_sum_sorted(A):
    row_len, col_len = len(A), len(A[0])
    ans = 0
    for i in range(row_len):
        for j in range(col_len):
            pf = getPF(tl,br)
            sum = pf[i][j]
            ans = max(ans, sum)
    return ans

print(max_2d_max_sub_matrix_sum_sorted(twoDArray))


#Rain water trapping Problem
#get maxleft and maxright for that index
#then water trapped is max(min(lmax,rmax)-i , 0)
#if negative then dont consider hence max used
#do not consider first and last blocks

#construct prefix max array and suffix max array first

def rain_water_trapped(A):
    p = [0 for i in range(len(A))]
    for v in A:
        if prev_max
        
#Min swaps required to bring all elements=x together 
#get no of x's in Array  = lenght l 
#build prefix array for each window of length l 
#now slide that windwo and swaps = length - noof x's in current window




##Given an binary array  - find the length of smallest subarray which when flipped will give us max no of 1's in array
#sol: replace 1's bu -1 and o by 1 and apply kadanes toget max subarray sum


#Given N array elements, find length of longest subarray which can be rearranged increasing order by 1





#Prime Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes
  
  
def SieveOfEratosthenes(n):
  
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
  
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
  
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
  
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            print(p)
  
  
# Driver code
if __name__ == '__main__':
    n = 20
    print("Following are the prime numbers smaller"),
    print("than or equal to", n)
    SieveOfEratosthenes(n)
    
    