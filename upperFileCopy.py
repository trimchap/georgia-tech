#---------------------------------------------------------
# take an input and output file as arguments. make a copy
# of the input file but uppercase all the characters
#---------------------------------------------------------
def to_upper_copy(outputfile, inputfile): 
    file1 = open(inputfile, 'r')
    file2 = open(outputfile, 'w')
    Lines = file1.readlines()
    for line in Lines:
        file2.writelines(line.upper())
    file1.close()
    file2.close()


# TEST
to_upper_copy("anOutputFile.txt", "anInputFile.txt")
print("--- anInputFile.txt ---")
with open("anInputFile.txt", 'r') as fin:
    print(fin.read())
print("--- anOutputFile.txt ---")
with open("anOutputFile.txt", 'r') as fin:
    print(fin.read())
