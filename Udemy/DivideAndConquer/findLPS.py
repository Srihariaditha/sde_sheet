# Longest Palindromic Susequence
################################################################

def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex or (startIndex == 0 and endIndex == 0):
        return 0

    elif startIndex == endIndex:
        return 1
    elif s[startIndex].lower() == s[endIndex].lower():
        return 2 + findLPS(s, startIndex+1, endIndex-1)
    else:
        op1 = findLPS(s, startIndex, endIndex-1)
        op2 = findLPS(s, startIndex+1, endIndex)
        return max(op1, op2)


print(findLPS('Epsllpe', 0, 6))
