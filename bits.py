import os
import pickle

def bits(f):
    bytes = (ord(b) for b in f.read())
    for b in bytes:
        for i in xrange(8):
            yield (b >> i) & 1



bitsToAnalise = 128*8;
statsDir = 'stats/'

grandPaDir = '/training'

for directory in os.listdir(os.getcwd()+ grandPaDir):

    if directory == ".DS_Store":
        continue
    parentDir = "/"+directory+"/"
    print(grandPaDir+parentDir)
    nameOfDir = directory
    currentCompDir = grandPaDir+parentDir
    statsFile = open(statsDir+nameOfDir+"_"+'bitsfile.txt','w')
    storageListDeList = []
    for filename in os.listdir(os.getcwd()+ currentCompDir):
        testFile = open(os.getcwd()+currentCompDir + filename,'r')
        path = (os.getcwd()+currentCompDir+ filename)
        pathDir = os.getcwd()+currentCompDir
        print(path)
        storageList = []
        storageList.append(filename)
        i = 0;
        for b in bits(testFile):
            if i < bitsToAnalise:
                storageList.append(b)
                i+=1
            else:
                break
        statsFile.writelines(str(storageList))
        storageListDeList.append(storageList)

    statsFilePickle = open((statsDir+nameOfDir+'_'+'bitspickle.txt'),'w')
    pickle.dump(storageListDeList,statsFilePickle)