###Ecoli
#This formats the ecoliInfile into a dense string that is easy to work with
with open ("Z:/Bioinformatics/lab3/files/ecoli.txt") as ecoliInfile:
    ecoliHeaderInfo=ecoliInfile.readlines()[:1:1]
    ecoliHeaderInfo=''.join(ecoliHeaderInfo)
    ecoliHeaderInfo=ecoliHeaderInfo.replace('>gi|', '')
    ecoliHeaderInfo=ecoliHeaderInfo.replace('|dbj|BA000007.2| Escherichia coli O157:H7 str. Sakai DNA, subset', '')
    
# prints out the ecoliHeaderInfo
print "**Ecoli**"
print ecoliHeaderInfo


###
