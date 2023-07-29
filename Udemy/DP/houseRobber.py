

#Top Down
def houseRobberTD(houses, curIndex, tempDict):
    if curIndex >= len(houses):
        return 0
    else:
        if curIndex not in tempDict:
          stealFirstHouse = houses[curIndex] + houseRobberTD(houses, curIndex+2, tempDict)
          skipFirstHouse = houseRobberTD(houses, curIndex+1, tempDict)
          tempDict[curIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempDict[curIndex]
    
houses = [ 6, 1,39, 45,7]
tempDict = {}
print houseRobberTD(houses, 0, tempDict);
print tempDict;

#Bottom Up
def houseRobberBU(houses):
    temp = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
       temp[i] = max(houses[i]+temp[i+2], temp[i+1])
       print temp
    return temp[0]
houses = [ 6, 1,39, 45,7]
print houseRobberBU(houses)

