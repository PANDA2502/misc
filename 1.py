from collections import Counter

def generateStrings(input):
    freqDict = Counter(input)
    print(freqDict)
    freq1 = [key for (key,count) in freqDict.items() if count==1 ]
    freg2 = [key for (key, count) in freqDict.items() if count >1]

    print (''.join(freq1))
    print (''.join(freg2))

input = "geeksforgeeks"
generateStrings(input)

list = [2,5,1,5,325,6,6,364,346,2342,26,36,23423,23]
list2 = ["cat","Dog","beef","woof","the eggs","seick"]
x = [x for x in list if x >10]
x2 = [x for x in list2 if 'e' in x]

print(list2 )
print(x2)