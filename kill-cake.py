import re
def solution(s):
    def allCharactersSame(s) :
        n = len(s)
        for i in range(1, n) :
            if s[i] != s[0]:
                return False
        return True
    allSameBool = allCharactersSame(s)
    if(allSameBool):
        return len(s)
    initial = 2
    answers = []
    lenghtStr = len(s)
    while(initial <= lenghtStr):
        sliceConstruct = slice(initial)
        x = re.findall(s[sliceConstruct], s)
        tempRes = len(x)*initial
        if(tempRes == len(s)):
            answers.append(len(x))
        initial = initial + 1
    return max(answers)
    
