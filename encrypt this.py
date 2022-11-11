"""
Description:

Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
        The first letter must be converted to its ASCII code.
        The second letter must be switched with the last letter
    Keepin' it simple: There are no special characters in the input.
"""
def encrypt_this(text):
    print(text)
    if(text == ""):
        return ""
    words = text.split(" ")
    newWords = []
    for word in words:
        if(len(word) == 1):
            newWords.append(str(ord(word[0])))
            continue
        if(len(word) == 2):
            newWords.append(str(ord(word[0])) + word[1])
            continue
        oldWord = word
        word = word[0] + word[len(word)-1:len(word)] + word[2:len(word)-1] + word[1]
        word = str(ord(word[0])) + word[1:]
        newWords.append(word)
    return " ".join(newWords)

