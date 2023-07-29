# House Robber
################################

def houseRobber(houses, currentIndex, solutionArray):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + \
            houseRobber(houses, currentIndex+2, solutionArray)
        skipFirstHouse = houseRobber(houses, currentIndex+1, solutionArray)
        if skipFirstHouse > stealFirstHouse:
            if currentIndex < len(houses)-1:
                solutionArray[currentIndex+1] = True
            if currentIndex+2 < len(houses):
                solutionArray[currentIndex+2] = False
            solutionArray[currentIndex] = False
            return skipFirstHouse
        else:
            solutionArray[currentIndex] = True
            if currentIndex < len(houses)-2:
                solutionArray[currentIndex+2] = True
            if currentIndex < len(houses)-1:
                solutionArray[currentIndex+1] = False
            return stealFirstHouse


l = [34, 56, 23, 67, 78]
s = {}
# l = [4, 12, 9]
# s2 = [False] * len(l)

print(houseRobber(l, 0, s))
print(s)
