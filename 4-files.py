#########################################################################
# File Input, For more, see: 
#	https://docs.python.org/2/tutorial/inputoutput.html
#########################################################################

## open file for reading, will need to specify full path 
infile = open("Z:/Bioinformatics/Python-Advanced/4-files.py")

print infile
print

print 'a',   # the comma says "don't go to next line"
print 'b',
print 
print

# print out each line of file; note that line ends with a '\n'
print "The contents of the file are: "
for line in infile :
  print line,

# close the file
infile.close()


# additional useful file functions (assuming open file stored in object infile):
infile.read() #- reads entire file as a single string
# infile.readline() - reads the next line of the file, as a string
# infile.readlines() - reads the entire file into a list of strings, with each
#                      element a line of the file

