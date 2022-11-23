#Josh Wenger

def letters(text):
    text = text.lower()
    abcs = 'qwertyuiopasdfghjklzxcvbnm'
    abcs = list(abcs)
    abcs.sort()
    alphabet = {}
    for letter in abcs:
        alphabet[letter] = 0

    for letter in text:
        if letter in alphabet.keys():
            alphabet[letter] += 1
    print(alphabet)
        

with open ('encryptedmac.txt', 'r+') as e:
    text = e.read()

letters(text)


        



