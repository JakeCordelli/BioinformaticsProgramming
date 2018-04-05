#######################################
# Python Basics: this is a comment
#######################################

# printing to the screen
print "Hello World!"    # works only in Python 2*
print 'Hello World'     # you can use single or double quotes for strings
print("Hello World!")   # you must use the 'print' function in Python 3*


# In Python 3, the full form of the print function is:
# print(objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#print("Hello", "World!", sep= ' ', end = '\n')  # does the same as above

# newline character:
print("Hello\nGoodbye")

# skip a line
print

# variables are not declared #
x = 4.2
y = 6
sum = x + y

# to print multiple objects, separate with commas
# (spaces are added to separate each object)
print "x =", x
print"y =", y
print "sum =", sum
print "sum =",  x + y  # print statement may include expressions

# use + for string concatenation and 'str' to convert objects to strings 
answer = "The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + "."
print(answer)

# variables can be numbers, characters, strings, or boolean values
x = "Bioinformatics"
print "Are you ready for some " + x + "?"

compare = 5 > 0   # compare is True
print "compare =", compare


########################################################################
# Exercise: Use two string variables to store your first and last name.
# Then create a third string variable that stores your full name, based
# on the first two strings, and output its value
########################################################################




