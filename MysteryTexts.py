#Josh Wenger

#message 1: class list
#message 2: Monty Python sketch titled "Argument Clinic"
#message 3: Doctor Who episode titled "Time and the Rani"
#message 4: the novel "Gadsby"
#message 5: a PressRadar article titled "Lindor and 21 teammates sign for 2018"

def charshift(char, shift):
    abcs = 'qwertyuiopasdfghjklzxcvbnm'
    char = char.lower()
    try:
        if char in abcs:
            if 97 <= (ord(char)+shift) <= 122:
               return chr(ord(char)+shift)
            elif (ord(char)+shift) >= 122:
                return chr(ord(char)+shift-26)
        elif char not in abcs:
            return char
    except:
        print('Incorrect item class.')


def ceaser(text, shift):
    shiftedlyst = [charshift(x, shift) for x in text]
    shiftedstr = "".join(shiftedlyst)
    return shiftedstr

def checker(text,shift):
    print(ceaser(text,shift))
    while True:
        correct = input("Can you read this text? (y/n)")
        if correct == "y":
            return True
        elif correct == "n":
            return False
        else:
            print("Invalid input")
            continue
def decode():
    file = input("Please input the name of a text file you'd like to decode:")
    with open(file, 'r+', encoding="ISO-8859-1") as f:
        coded = f.read()
    for shift in range(1,26):
        if checker(coded,shift) == True:
            break
decode()




