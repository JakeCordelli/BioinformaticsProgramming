ecoli = open("C:/Users/Samantha Dauphinais/Documents/Intro BioInformatics/lab3/files/ecoli.txt")
human = open("C:/Users/Samantha Dauphinais/Documents/Intro BioInformatics/lab3/files/human.txt")
raoultella = open("C:/Users/Samantha Dauphinais/Documents/Intro BioInformatics/lab3/files/raoultella.txt")
samples = open("C:/Users/Samantha Dauphinais/Documents/Intro BioInformatics/lab3/files/samples.txt")
zika = open("C:/Users/Samantha Dauphinais/Documents/Intro BioInformatics/lab3/files/zika.txt")

import re
pattern = re.compile("[GA][GA]C[AT][AT]G[TC][TC]")

def readSequence(x):
    x = x.read()
    i = x.find('\n')
    x = x[i:]
    x = x.replace('\n', '')
    return (x)


dic = {"ecoli": readSequence(ecoli), "human": readSequence(human), "raoultella": readSequence(raoultella), "zika": readSequence(zika)}
print "Length of ecoli sequence: " + str(len(dic["ecoli"]))
print "Length of human sequence: " + str(len(dic["human"]))
print "Length of raoultella sequence: " + str(len(dic["raoultella"]))
print "Length of zika sequence: " + str(len(dic["zika"]))



s = samples.readlines()
s2 = ""
for i in range(len(s)):
    n = s[i].index(':')
    j = s[i].index('\n')
    s2 = s2 + s[i][n+2:j] + ' '

s3 = s2.split()
print s3[0:3]

ecoliCount = 0
humanCount = 0
raoultellaCount = 0
zikaCount = 0
unknownCount = 0

for i in s3:
    if(i in dic['ecoli']):
        ecoliCount = ecoliCount +1
    elif(i in dic['human']):
        humanCount = humanCount +1
    elif(i in dic['raoultella']):
        raoultellaCount =raoultellaCount +1
    elif(i in dic['zika']):
        zikaCount = zikaCount +1
    else:
        unknownCount = unknownCount +1


print "Number of samples belonging to ecoli: " + str(ecoliCount)
print "Number of samples belonging to human: " + str(humanCount)
print "Number of samples belonging to raoultella: " + str(raoultellaCount)
print "Number of samples belonging to zika: " + str(zikaCount)
print "Number of unknown samples: " + str(unknownCount)
    

ecoli.close()
human.close()
raoultella.close()
samples.close()
zika.close()

