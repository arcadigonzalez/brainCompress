from __future__ import print_function
import backports.lzma as lzma
import gzip
import zlib
import zipfile
import bz2
import os
import time
import pickle




statsDir = 'stats/'

grandPaDir = '/training/'
lastDirs = ['singles']
for directory in os.listdir(os.getcwd()+ grandPaDir):
    if directory == ".DS_Store":
        continue
    parentDir = "/"+directory+"/"
    print(grandPaDir+parentDir)
    nameOfDir = directory
    currentCompDir = grandPaDir+parentDir
    statsFile = open(statsDir+nameOfDir+"_"+'statsfile.txt','w')
    storageListDeList = []
    for filename in os.listdir(os.getcwd()+ currentCompDir):
        testFile = open(os.getcwd()+currentCompDir + filename,'r')
        path = (os.getcwd()+currentCompDir+ filename)
        pathDir = os.getcwd()+currentCompDir
        print(path)

        storageList = []

        #testFileName = "1257-0.txt"
        storageList.append(filename)
        uncompSize = float(os.path.getsize(path))
        storageList.append(uncompSize)


        start = time.time()
        compressionMethod = 'ZIP_STORED'
        compressedName = (path + compressionMethod)
        with zipfile.ZipFile(compressedName,'w',zipfile.ZIP_STORED) as newFile:
            newFile.write(path)
            newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)

        start = time.time()

        compressionMethod = 'ZIP_DEFLATED'
        compressedName = (path + compressionMethod)
        with zipfile.ZipFile( compressedName,'w',zipfile.ZIP_DEFLATED) as newFile:
            newFile.write(path)
            newFile.close()
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)


        start = time.time()

        #bzip modes
        compressionMethod = 'BZIPPED'
        compressedName = (path + compressionMethod)
        with bz2.BZ2File( compressedName,'w',zipfile.ZIP_DEFLATED) as newFile:
            newFile.write(testFile.read())
            newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)



        #lzma modes

        #standard filter values
        dict_size = 1610612736
        lc = 1
        lp = 0
        pb = 2
        mode = lzma.MODE_NORMAL
        nice_len = 273
        mf = lzma.MF_BT2
        depth = 0

        std_LZMA2_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb":pb , "mode":mode,  "mf":mf, "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
        start = time.time()
        compressionMethod = 'LZMA_STD'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open( compressedName,'wb', filters=std_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)


        start = time.time()


        std_LZMA1_filter = [
            {"id": lzma.FILTER_LZMA1,  "lc": lc, "lp":lp, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
        compressionMethod = 'LZMA1_STD'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(compressedName,'wb',filters=std_LZMA1_filter, format=lzma.FORMAT_ALONE)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)


        start = time.time()
        LZMA2_DELTA1_filter = [
            {"id": lzma.FILTER_DELTA, "dist": 1},
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
        compressionMethod = 'LZMA2_DELTA1'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_DELTA1_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove( compressedName)


        start = time.time()
        LZMA2_HLP_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": 0, "lp":4, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
        compressionMethod = 'LZMA2_HLP'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_HLP_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove( compressedName)


        start = time.time()
        LZMA2_HLC_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": 4, "lp":0, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
        compressionMethod = 'LZMA2_HLC'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_HLC_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)


        start = time.time()
        LZMA2_HPB_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb": 4 , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
        compressionMethod = 'LZMA2_HPB'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_HPB_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)


        start = time.time()
        BJC = lzma.FILTER_ARM

        BJC_LZMA2_filter = [
            {"id": BJC},
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb": pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
        compressionMethod = 'BJC_ARM_LZMA2'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(compressedName)


        start = time.time()
        BJC = lzma.FILTER_ARMTHUMB
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = 'BJC_ARMTHUMB_LZMA2'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(  compressedName)


        start = time.time()
        BJC = lzma.FILTER_IA64
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = 'BJC_IA64_LZMA2'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(  compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(  compressedName)


        start = time.time()
        BJC = lzma.FILTER_POWERPC
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = 'BJC_POWERPC_LZMA2'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(  compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(  compressedName)


        start = time.time()
        BJC = lzma.FILTER_SPARC
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = 'BJC_SPARC_LZMA2'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(  compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(  compressedName)


        start = time.time()
        BJC = lzma.FILTER_X86
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = 'BJC_X86_LZMA2'
        compressedName = (path + compressionMethod)
        testFile.close()
        testFile = open(path,'r')
        newFile = lzma.open(  compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(  compressedName)


        #gzip modes
        start = time.time()
        testFile = open(path,'r')
        compressionMethod = 'GZIPPED'
        compressedName = (path + compressionMethod)
        newFile = gzip.open(   compressedName,'w')
        newFile.write(testFile.read())
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(  compressedName)


        start = time.time()
        testFile = open(path,'r')
        compressionMethod = 'ZLIBBED'
        compressedName = (path + compressionMethod)
        newFile = open(   compressedName,'w')
        compressedContent = zlib.compress(testFile.read(),9)
        newFile.write(compressedContent)
        newFile.close()
        print (compressionMethod+": "+str(float(os.path.getsize(compressedName))/1024) +" Kb " + \
               str(float(os.path.getsize(compressedName))/float(os.path.getsize(path))))
        print(str((time.time()-start)*1000) + " miliseconds")
        size = float(os.path.getsize(compressedName))
        tm = time.time()-start
        storageList.append(compressionMethod)
        storageList.append(size)
        storageList.append(size/uncompSize)
        storageList.append(tm)
        print()
        os.remove(  compressedName)
        storageListDeList.append(storageList)
        statsFile.writelines(str(storageList))
        statsFile.write("\n")


    print(storageListDeList)
    statsFilePickle = open((statsDir+nameOfDir+'_'+'statspickle.txt'),'w')
    pickle.dump(storageListDeList,statsFilePickle)

    statsFile.close()


