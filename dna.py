inFile = open("dna.txt", "r")
sequences = inFile.read()
sequence = sequences.split("\n\n")
for i in range(len(sequence)):
    sequence[i] = sequence[i].replace("\n", "")
    print (f"{i}: {sequence[i]}")
    print("")
inFile.close()