#########################################################################
# Functions in python
#   As with if statements and loops, use indentation rather than braces
#   to create a block of code
#   return statements are optionally used to return a value
#########################################################################

def welcome() :
  print "This script demonstrates how to write functions in Python"

def add(x,y) :
  return x + y

# multi-line function (all line are indented)
def add1(x) :
  x = x + 1
  return x	
 

welcome()  # display welcome message
print "add(3,4) = ", add(3,4)
print "add1(99) = ", add1(99)


