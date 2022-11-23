#Decodes ceaser shift by suggesting the most likely solution based on letter frequency analysis.

letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

abcs = 'qwertyuiopasdfghjklzxcvbnm'
abcs = ''.join(sorted(abcs))
txt = input("Input text you would like to decode.")

def charshift(char, shift):
   char = char.lower()
   if char in abcs:
      if 97 <= (ord(char)+shift) <= 122:
         return chr(ord(char)+shift)
      elif (ord(char)+shift) > 122:
         return chr(ord(char)+shift-26)
      elif (ord(char)+shift) < 97:
         return chr(ord(char)+shift+26)  
   elif char not in abcs:
      return char
def ceaser(text, shift):
   shiftedlyst = [charshift(x, shift) for x in text]
   shiftedstr = "".join(shiftedlyst)
   return shiftedstr
freqlyst = []
freqlystsum = 0
for x in range(26):
   for char in ceaser(txt, x):
      if char in abcs:
         freqlystsum += letterGoodness[abcs.index(char)]
   freqlyst.append(freqlystsum)
   freqlystsum = 0
index = freqlyst.index(max(freqlyst))   
print(ceaser(txt,index).upper())
