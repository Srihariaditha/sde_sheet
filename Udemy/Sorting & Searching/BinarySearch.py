#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Searching algorithms - Binary Search
import math
def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1
        



custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))
# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M               E
#  S  M      E
#        SM  E
#            SME

#Given N tasks and K workers and time taken for each task find min time in which we can complete all tasks
#A single worker can do only continous set of tasks
#All workers start their assigned tasks at same time
#A task can only be assigned to single worker
N=15
k=4
t = [3,5,1,7,8,2,5,3,10,1,4,7,5,4,6]

def get_min_time(N, K , A):
    low = max(A)
    high = sum(A)
    ans = high
    while (low <= high):

        m = (low + high)/2
        print(low, high, m)

        if check_workers(m,A,N,K):
            ans = m
            high = m-1
        else:
            low=m+1
    return ans
def check_workers(time, A, N,K):
    s,c = 0,0
    for v in A:
        s = s + v
        if s>time:
            s=v
            c+=1
    if s!=0:
        c+=1
    if c<=k:
        return True
    else:
        return False
print(get_min_time(N,k,t))

#Given N cows and M stalls, all m stalls are on x-axis at different locations. Place all cows such that distance between any two cows is maximized.
#Only 1 cow per stall
#all cows has to be placed
N = 3
M = 5
s = [1,2,4,8,9]
minAdj = lambda s: [(s[i+1]-s[i]) for i in range(0, len(s)-1)]
def get_min_distance_cows(s, N, M):
    low = min(minAdj(s))
    high = s[M-1]-s[0]
    ans = low
    while(low <=high):
        mid = (low+high)/2
        print(low, high, mid, ans)
        if check_stalls(s, N, mid):
            low=mid+1
            ans=low
        else:
            high = mid-1
    return ans

def check_stalls(s, n, dis):
    last_cow, c = s[0], 1
    for v in s[1:]:
        if v-last_cow>dis:
            c+=1
            last_cow=v
        if c==n:
            return True
    return False

print(get_min_distance_cows(s,N,M))

#Every element occurs twice except for 1, find that element
#XOR is one solution
#use BS
S= [3,3,5,5,6,6,10,19,19,23,23]




#Given an array which is formed by rotating a distinct sorted array K times, find an element in this rotated array
#split array into two parts and search for element either in first part or second part using BS
S= [11,14,15,16,-1,-3,-5,-7,1]
K =4        


#Given N find SQRT(N)


#Check Pairs in distinct sorted array
#use Hash - but Space 

def check_pair_sum(A,k):
    l,h = 0, len(A)-1
    while(l<h):
        cur_sum = A[l]+A[h]
        if(cur_sum==k):
            return True
        elif(cur_sum >k):
            h -= 1
        else:
            l += 1
    return False
            
print(check_pair_sum([1,2,3,4,5],8))    
    
        
#Ath Magical Number
#Kth index element in unsorted array
#simple 2 pointer    