import os

genomeNameList = []
genomeTypeList = []
genomePerFileDict = {}
genomeTypeTotalsDict = {}

mainWriteLines = []
totalWriteLines = []

def genomeNameListCreator():
    choice = input("Give rs-number of a genome (press q to quit): ")

    while choice != 'q':
        genomeNameList.append(choice)
        choice = input("Give rs-number of a genome (press q to quit): ")

def genomeTypeListCreator():
    choice = input("Give type of a genome (press q to quit): ")

    while choice != 'q':
        genomeTypeList.append(choice)
        choice = input("Give type of a genome (press q to quit): ")

def createDictionaries():
    for genomeName in genomeNameList:
        genomePerFileDict[genomeName] = ""

    for genomeName in genomeNameList:
        genomeTypeTotalsDict[genomeName] = {}
        for genomeType in genomeTypeList:
            genomeTypeTotalsDict[genomeName][genomeType] = 0

def createFiles(dataLocation, outputLocation, totalFile):
    mainFileName = input("Enter the name for the main file (do not end the name with .txt): ") + ".txt"
    if totalFile == True:
        totalFileName = ''
        totalFileName = input("Enter the name for the totals file (do not end the name with .txt): ") + ".txt"
    
    print('\n' + "!When entering the position start counting from 1 not from 0" + '\n')
    
    genomeNamePosition = int(input("Please input the position of the genome name in the data (the column number): ")) -1
    genomeTypePosition = int(input("Please input the position of the genome type in the data (the column number): ")) -1

    for file in os.listdir(dataLocation):
        if file.endswith(".txt"):
            if file != mainFileName:
                if file != totalFileName:
                    print("reading " + file)
                    readFile = open(os.path.join(dataLocation, file), 'r')
                    Lines = readFile.readlines()
                    for Line in Lines:
                        words = Line.split()
                        if words[genomeNamePosition] in genomeNameList:
                            genomeTypeTotalsDict[words[genomeNamePosition]].update({words[genomeTypePosition]: genomeTypeTotalsDict[words[genomeNamePosition]][words[genomeTypePosition]]+1})
                            genomePerFileDict.update({words[genomeNamePosition]:words[genomeTypePosition]})
                    mainLinesPrint = []
                    for x in genomePerFileDict.values():
                        mainLinesPrint.append(str(x))
                    
                    mainLinesWrite = str(file) + " " + (" ".join(mainLinesPrint))
                    mainWriteLines.append(mainLinesWrite)

    for x in genomeTypeTotalsDict:
        totalline = x
        totallinenumbers = []
        for y in genomeTypeTotalsDict[x]:
            totallinenumbers.append(str(genomeTypeTotalsDict[x][y]))
        totallilines = totalline + " " +  " ".join(totallinenumbers)
        totalWriteLines.append(totallilines)
    
    with open(os.path.join(outputLocation, mainFileName), 'w') as f:
        f.write('FileName ')
        f.write(' '.join(genomeNameList))
        f.write('\n')
        for Line in mainWriteLines:
            f.write(f"{Line}\n")

    if totalFile == True:
        with open(os.path.join(outputLocation, totalFileName), 'w') as f:
            f.write('rs-number ')
            f.write(' '.join(genomeTypeList))
            f.write('\n')
            for Line in totalWriteLines:
                f.write(f"{Line}\n") 

def startup():
    genomeNameListCreator()
    genomeTypeListCreator()
    createDictionaries()
    
    DataFilesLocation = input("Enter the folder location of your data files: ")
    OutputFilesLocation = input("Enter the folder for the location of your output files: ")
    if not os.path.exists(OutputFilesLocation):
        os.makedirs(OutputFilesLocation)
    
    requireTotalFiles = input("Do you want to count the totals for each type per genome (Y for yes, N for no): ")
    if requireTotalFiles == "Y":
        requireTotalFiles = True
    elif requireTotalFiles == "N":
        requireTotalFiles = False
    else:
        print("Please enter a valid answer")
        requireTotalFiles = input("Do you want to count the totals for each type per genome (Y for yes, N for no): ")

    createFiles(DataFilesLocation, OutputFilesLocation, requireTotalFiles)
    print("Files Created")

startup()