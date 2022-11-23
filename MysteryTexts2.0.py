#Josh Wenger

#message 1: class list
#message 2: Monty Python sketch titled "Argument Clinic"
#message 3: Doctor Who episode titled "Time and the Rani"
#message 4: the novel "Gadsby"
#message 5: a PressRadar article titled "Lindor and 21 teammates sign for 2018"

#Shifts a given character (char) by the number of letters given in shift
def charshift(char, shift):
    abcs = 'qwertyuiopasdfghjklzxcvbnm'
    char = char.lower()
    try:
        if char in abcs:
            if 97 <= (ord(char)+shift) <= 122:
               return chr(ord(char)+shift)
            elif (ord(char)+shift) > 122:
                return chr(ord(char)+shift-26)
            elif (ord(char)+shift) < 97:
                return chr(ord(char)+shift+26)
        elif char not in abcs:
            return char
    except:
        print('Incorrect item class.')

#Calls charshift on any amount of text. It creates a list of the shifted characters, then joins them into a string.
def ceaser(text, shift):
    shiftedlyst = [charshift(x, shift) for x in text]
    shiftedstr = "".join(shiftedlyst)
    return shiftedstr

#Calls ceaser and allows the user to input whether it made the text readable.
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
        
#Counts the prevalence of each letter and creates a list that sorts the letters from most to least prevalent.
#The final line in this block creates the sorted list. It specifies that it wants the list to consist of keys from the dictionary "alphabet".
#The lambda creates a sort of temporary function specifying that it should sort by the values at each given key (k).
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
    return sorted(alphabet.keys(), key=lambda k: alphabet[k], reverse = True)
        

#Goes through the possible shifts until the user says that it is readable (because the checker function will return True).
#It goes through the shifts in order of the distance between the most prevalent letters and 'e'.
def decode():
    file = input("Please input the name of a text file you'd like to decode:")
    with open(file, 'r+', encoding="ISO-8859-1") as f:
        coded = f.read()
    letters_by_prev = letters(coded)
    for letter in letters_by_prev:
        shift = ord('e') - ord(letter)
        if checker(coded,shift) == True:
            break

decode()




