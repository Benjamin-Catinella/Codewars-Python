"""
Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
"""
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaC = ['']*len(alpha)
for i,letter in enumerate(alpha):
    alphaC[i] = letter.upper()

def find_missing_letter(chars):
    try:
        index = alpha.index(chars[0])
        j=0
        for i in range(index,len(alpha)):
            if chars[j] != alpha[i]:
                return alpha[i]
            j+=1
    except:
        index = alphaC.index(chars[0])
        
        j=0
        for i in range(index,len(alpha)):
            if chars[j] != alphaC[i]:
                return alphaC[i]
            j+=1
