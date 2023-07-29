# Largest Common Subsequence
################################


def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1+findLCS(s1, s2, index1+1, index2+1)
    else:
        op2 = findLCS(s1, s2, index1+1, index2)
        op3 = findLCS(s1, s2, index1, index2+1)
        return max(op2, op3)


s1 = 'elephant'
s2 = 'elehant'
print(findLCS(s1, s2, 0, 0))
