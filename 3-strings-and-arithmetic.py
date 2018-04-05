######################################################################
# arithmetic follows C++/Java rules (i.e., watch out for integer division)
# Note that integer division is not a problem in Python 3*
######################################################################

print "5 / 2 = ", 5/2  # integer division
print "5 % 2 = ", 5%2  # mod operator returns the remainder
print "5.0 / 2 = ", 5.0/2  
print "5.0 // 2 = ", 5.0 // 2  # integer (floor) division
print "3**2 = ", 3**2
print

# C++/Java shortcuts may be used, e.g.
x = 3
x+= 2
print "x = ", x
print

######################################################################
# string operations
# see http://www.tutorialspoint.com/python/python_strings.htm for more
######################################################################
str = "Hello, how are you?"
print "string = ", str
print "length = ", len(str)
print "First letter", str[0] # index starts at 0

# ranges of strings can be specified (this is known as slicing)
# str[a:b] returns characters starting at index 'a' and up to
# but NOT including index 'b'
print "First three letters: ", str[0:3] 

# all uppercase
print "Uppercase string: ", str.upper()
# all lowercase
print "Lowercase string: ", str.lower()

# count number of 'e's in the string (case sensitive count)
numE = str.count('e')
print "Number of 'e's = ", numE

# find substring
print "Index of ' ': ", str.find(' ') # index of first occurence if found
print "Index of ABC : ", str.find("ABC") # return -1 if not found

# does string contain a substring?
print "string contains \"how\":", "how" in str
print "string contains \"where\":", "where" in str


######################################################################
# Exercise:
# Prompt the user to enter a DNA sequence, and count the number of
# As, Cs, Gs, and Ts in the sequence
######################################################################


sequence=raw_input("Enter a DNA sequence: ")
sequence=sequence.upper()
numA=sequence.count('A')
numT=sequence.count('T')
numC=sequence.count('C')
numG=sequence.count('G')
print "Number of As, Ts, Cs, and Gs is: ", numA, numT, numC, numG
