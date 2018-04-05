#Jake Cordelli
#2/10/17
#Bioinformatics


#create a method that takes in the input from the file and converts
#the input into a readable and formatted string for the program to use   

###Ecoli
#This formats the ecoliInfile into a dense string that is easy to work with
with open ("Z:/Bioinformatics/lab3/files/ecoli.txt") as ecoliInfile:
    ecoliInputData=ecoliInfile.readlines()[1::]
    ecoliData=''.join(ecoliInputData)
    ecoliData=ecoliData.replace('\n', '')
    
# prints out the ecoliData as well as information about it
print "**Ecoli**"
print "The length of this Ecoli sequence is:",len(ecoliData)
print "The sequence is: "
print ecoliData
###

print

###Zika
#This formats the zikaInfile into a dense string that is easy to work with
with open ("Z:/Bioinformatics/lab3/files/zika.txt") as zikaInfile:
    zikaInputData=zikaInfile.readlines()[1::]
    zikaData=''.join(zikaInputData)
    zikaData=zikaData.replace('\n', '')
# prints out the zikaData as well as information about it
print "**Zika**"
print "The length of this Zika sequence is:",len(zikaData)
print "The sequence is: "
print zikaData
###

print

###Raoultella
#This formats the raoultellaInfile into a dense string that is easy to work with
with open ("Z:/Bioinformatics/lab3/files/raoultella.txt") as raoultellaInfile:
    raoultellaInputData=raoultellaInfile.readlines()[1::]
    raoultellaData=''.join(raoultellaInputData)
    raoultellaData=raoultellaData.replace('\n', '')
# prints out the raoultellaData as well as information about it
print "**Raoultella**"
print "The length of this Raoultella sequence is:",len(raoultellaData)
print "The sequence is: "
print raoultellaData
###

print

###Human
#This formats the humanInfile into a dense string that is easy to work with
with open ("Z:/Bioinformatics/lab3/files/human.txt") as humanInfile:
    humanInputData=humanInfile.readlines()[1::]
    humanData=''.join(humanInputData)
    humanData=humanData.replace('\n', '')
# prints out the humanData as well as information about it
print "**Human**"
print "The length of this Human sequence is:",len(humanData)
print "The sequence is: "
print humanData
###

print

###Sample
#This formats the sampleInfile into a dense string that is easy to work with
with open ("Z:/Bioinformatics/lab3/files/samples.txt") as sampleInfile:
    sampleInputData=sampleInfile.readlines()
    sampleData=''.join(sampleInputData)
for i in range (0, 106):
    x=str(i)
    sampleString='sample '+x+':'
    sampleData=sampleData.replace(sampleString,'')
sampleData=sampleData.replace(' ', '')
# prints out the sampleData as well as information about it
print "**Sample**"
print "The length of this Sample sequence is:",len(sampleData)
print "The sequence is: "
print sampleData
###


###I was attempting to code a way to compare the sample sequences with
#the other sequences, however I couldn't figure out how to do it.
#I attempted to code it as follows below, but I couldn't figure out
#how to compare each individual line of the sample string.
humanCount=0
ecoliCount=0
zikaCount=0
raoultellaCount=0

for line in sampleData:
    if (sampleData in humanData):
        print true
        humanCount+=1
    if (sampleData in ecoliData):
        print true
        ecoliCount+=1
    if (sampleData in zikaData):
        print true
        zikaCount+=1
    if (sampleData in raoultellaData):
        print true
        raoultellaCount+=1

print "The sequence contains: "
print "Human: ", humanCount
print "Ecoli: ", ecoliCount
print "Zika: ", zikaCount
print "Raoultella: ", raoultellaCount


# Dictionary
sequenceElement ={"Human": humanData, 
            "Ecoli": ecoliData,
            "Zika": zikaData,
            "Raoultella": raoultellaData,
            "Sample": sampleData}


