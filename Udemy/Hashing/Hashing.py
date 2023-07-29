#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

def mod(number, cellNumber):
    return number % cellNumber


# print(mod(400, 24))


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

print(modASCII("ABC", 24))

#Given a array check subarray with sum 0
#create a prefix matrix with sum after adding each element and see if two sums match - check for repeating elements
#a signle element is also a subarray
#if there is a zero in pf array then also  
S= [2,2,1,-3,4,3,1,-2,-3,]


#Check if there is a repeating element in array
#sort and check - O(NlogN)
#Hashset

#Find length of longest subarray whose sum is zero
#hashing those lengths which are zero sums


#Find num of right angled traingles that can be formed from N co-ordinate poitns
#find frequencies of x and y coordiantes s.t they form RT

#Find no of rectangles with Npoints parallel to x and y axis
#Use TreeMap
