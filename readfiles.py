# TODO: write inputs for everything user can adjust

# import OS
import glob, os

list = ['GSA-rs79269225', 'rs8079271', 'exm2272575', 'rs479742', 'GSA-rs115718041', 'rs7214366']
slist = ['AA', 'AB', 'BB', 'NC']
writelines = []
totaldict =	{
    "GSA-rs79269225": {
        "AA" : 0,
        "AB" : 0,
        "BB" : 0,
        "NC" : 0
    },
    "rs8079271": {
        "AA" : 0,
        "AB" : 0,
        "BB" : 0,
        "NC" : 0
    },
    "exm2272575": {
        "AA" : 0,
        "AB" : 0,
        "BB" : 0,
        "NC" : 0
    },
    "rs479742": {
        "AA" : 0,
        "AB" : 0,
        "BB" : 0,
        "NC" : 0
    },
    "GSA-rs115718041": {
        "AA" : 0,
        "AB" : 0,
        "BB" : 0,
        "NC" : 0
    },
    "rs7214366": {
        "AA" : 0,
        "AB" : 0,
        "BB" : 0,
        "NC" : 0
    }
}
maindict = {
    "GSA-rs79269225": 0,
    "rs8079271": 0,
    "exm2272575": 0,
    "rs479742": 0,
    "GSA-rs115718041": 0 ,
    "rs7214366": 0,
}

# set directory here
directory = "/home/hydra/Documents/python readfile script"

for file in os.listdir(directory):
    if file.endswith(".txt"):
        if file != 'writefile.txt':
            if file != 'TotalsFile.txt':
                print(os.path.join(directory, file))
                file1 = open(os.path.join(directory, file), 'r')
                Lines = file1.readlines()
                count = 0
                mainlines = ''
                mainlines += str(file)
                for line in Lines:
                    count += 1
                    words=line.split()
                    if words[0] in list:
                        # print("ok")
                        totaldict[words[0]].update({words[3]: totaldict[words[0]][words[3]]+1})
                        maindict.update({words[0]:words[3]})
                        # print(totaldict)
                        # print(maindict)
                mainlinese = []
                for x in maindict.values():
                    mainlinese.append(str(x))

                mainilines = mainlines + " " + (" ".join(mainlinese))
                writelines.append(mainilines)


with open(os.path.join(directory, 'writefile.txt'), 'w') as f:
    f.write('FileName ')
    f.write(' '.join(list))
    f.write('\n')
    for writeline in writelines:
        f.write(f"{writeline}\n")

# print(totaldict)

with open(os.path.join(directory, 'TotalsFile.txt'), 'w') as f:
    f.write('rs-number ')
    f.write(' '.join(slist))
    f.write('\n')
    totalwritelines = []
    for x in totaldict:
        totalline = x
        # print(totalline)
        totallinenumbers = []
        for y in totaldict[x]:
            totallinenumbers.append(str(totaldict[x][y]))
        # print(totallinenumbers)
        totallilines = totalline + " " +  " ".join(totallinenumbers)
        totalwritelines.append(totallilines)
    for totalwriteline in totalwritelines:
        f.write(f"{totalwriteline}\n")