"""
https://www.codewars.com/kata/5842df8ccbd22792a4000245
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

Kata.expandedForm(12); # Should return "10 + 2"
Kata.expandedForm(42); # Should return "40 + 2"
Kata.expandedForm(70304); # Should return "70000 + 300 + 4"
"""
def expanded_form(num):
    numStr = str(num)
    power = len(numStr)-1
    numToPowerMap = []
    finalstring = ""
    for i, digit in enumerate(numStr):
        if(int(digit) == 0):
            power -= 1
            continue
        else:
            numToPowerMap.append([int(digit),power])
        power -= 1

    additionsList = []
    for num,power in numToPowerMap:
       additionsList.append(num * (10**power))
    
    for i,s in enumerate(additionsList):
        finalstring += str(s)
        if(i < len(additionsList)-1):
            finalstring += " + "

    return finalstring


print(expanded_form(788056))
print(expanded_form(900000))
print(expanded_form(155500))
