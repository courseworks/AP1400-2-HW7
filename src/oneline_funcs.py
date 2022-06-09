
def adjacentElementsProduct(inputArray):
    return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))

def allLongestStrings(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]

def checkPalindrome(inputString):
    return inputString == inputString[::-1]

def commonCharacterCount(s1, s2):
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))

def areSimilar(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2

def palindromeRearranging(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

def arrayReplace(i, e, s):
    return [x if x!=e else s for x in i]

def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])

def alphabeticShift(inputString):
    return "".join(chr(ord(i)+1) if i != "z" else "a" for i in inputString)

def firstDigit(inputString):
    return [ int(i) for i in inputString if i.isdigit() ][0]