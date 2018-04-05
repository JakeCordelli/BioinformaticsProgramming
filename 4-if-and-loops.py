######################################################################
# If statements, similar to Java/C++ but
# - no braces, the Python interpreter depends on indentation to
#       identify blocks
# - a colon (:) is used after each condition
# - elif is used instead of elseif
######################################################################

# Note: the elif and else statements are optional
# what happens if the final print statement is indented?
num = 69
if (num > 3) :
    print "number is > 3"
elif (num < 3) :
    print "number is < 3"
else :
    print "number is 3"
print "End if"  

print

# for loop example, using range to create a list of integers
# range(start,stop,step = 1) generates a list of numbers where:
#   start - the first number
#   stop - the sequence stops BEFORE reaching this number
#   step - difference between each number

# loop through numbers 3-5
for i in range(3,10,1):
    print(i)

print
print

# for loop example, iterating over each element of a string
str = "Hello"
for ch in str:
    print(ch)

print
print

# Tuples are a collection of items, like an array or list. 
# Tuples are immutable (the items cannot be changed directly). 
# Rules for concatenation and slicing apply.

words = ("hi", "bye", "why")
print words
print "number of words = ", len(words)
print

# for loop example, iterating over each element of a tuple
nums = (5,8,11)
for i in nums :
    print i


############################################################
# Exercise: use a for loop to add the  numbers between 1-10
# and display the result
############################################################
