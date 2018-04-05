#########################################################################
# A dictionary is a way to store key-value pairs, such as
# word-definition pairs, though this need not be the interpretation 
# 
# With a dictionary, it is easy to look up a 'key' and get the 'value'
#
# Rules: keys MUST be unique and immutable
# More info: http://www.tutorialspoint.com/python/python_dictionary.htm
#########################################################################

# format for setting up a dictionary:
d = {"Key1": "Value1", "Key2": "Value2"}
print "dictionary: ", d
print "d['Key1'] = ", d['Key1']
print

# more practical example
email = {"Dancik": "dancikg@easternct.edu", 
	  "Tasneem": "TasneemS@easternct.edu",
	  "Rosiene": "RosieneJ@easternct.edu",
	  "Tu": "tuH@easternct.edu",
	  "Lin:": "LINJ@easternct.edu"}

print "keys = ", email.keys()
# we can add a new value
email['Gao'] = "GaoK@easternct.edu" 
print "keys = ", email.keys()

print "Please e-mail Dr. Dancik at " + email["Dancik"]
print

###########################################################################
# Exercise: 
# 1. Create a DNA complement dictionary that maps each nucleotide 
#    character to its complementary character. 
# 2. Use this dictionary to output the complement of the sequence ACGTGA 
##########################################################################


