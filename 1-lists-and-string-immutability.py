########################################################################
# Strings and tuples are immutable (their elements cannot be changed)
########################################################################

word = "hello"
print word
print
#word[0] = 'H' # produces an error
 

################################################
# Methods for changing a character of a string
################################################
 
#1. Using the replace function
#   Note that the replace function creates a new string with the specified 
#   substring replaced, and returns the new string. Therefore, word.replace() 
#   on its own does not change the value of a string. However, we can assign 
#   the new string to a variable

print "Change word using replace: "
print "word = " + word
print "call word.replace('h', 'H')"
print "word = " + word
print "call word = word.replace('h', 'H')"
word = word.replace('h', 'H')
print "word = " + word
print
 
# 2. You can also use string concatenation and slicing:

print "Change word using string concatenation and slicing" 
word = "hello"
print "word = " + word
print "call word = \"H\" + word[1:]"
word = "H" + word[1:]   # replaces the first character 
print "word = " + word 
print

# 3. Convert the string to a list object and then convert it back to a string.
# A list is a essentially a tuple (a collection of objects), but tuples 
# are immutable while lists are not.

# A list is specified by including a collection in square brackets, as
# in the code below:
 
l = ["hi", "fly", "bye"]
print "l = ", l
print "change first element, using slicing"
l[0] = "Hello"  # change the first element
print "l = ", l
print

print "demonstrate insert and remove"
l.insert(0, "high") # inserts object before the specified index 
print "l = ", l
l.remove("high") # remove first occurence of object
print "l = ", l
print

# The join function is a string function that concatenates elements of a list 
# or tuple, which are separated by the specified character or string. Note: 
# the elements of the list or tuple must be characters or strings.

print "'-'.join(l) = " + '-'.join(l)    # outputs hi-fly-bye
print
 
# Putting this all together, we can modify a character of a string as follows:
print "modify a string by converting to a list, modifying, and converting back to a string"
word = "hello"   # initial string
print "word = " + word
l = list(word)   # convert to list
l[0] = "H"	# change first character
word = ''.join(l)  # convert back to string (no spaces between each character)
print "word = " + word
 
