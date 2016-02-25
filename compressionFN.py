from __future__ import print_function
import backports.lzma as lzma
import gzip
import zlib
import zipfile
import bz2



def compressSingle (fileName, compressionMethod):

    testFile = open(fileName,'r')

    #standard filter values
    dict_size = 1610612736
    lc = 1
    lp = 0
    pb = 2
    mode = lzma.MODE_NORMAL
    nice_len = 273
    mf = lzma.MF_BT2
    depth = 0


    #Filters for various LZMA compressions
    BJC = lzma.FILTER_ARM
    BJC_LZMA2_filter = [
            {"id": BJC},
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb": pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
    ]
    LZMA2_HPB_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb": 4 , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
    std_LZMA2_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb":pb , "mode":mode,  "mf":mf, "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
    std_LZMA1_filter = [
            {"id": lzma.FILTER_LZMA1,  "lc": lc, "lp":lp, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
    LZMA2_DELTA1_filter = [
            {"id": lzma.FILTER_DELTA, "dist": 1},
            {"id": lzma.FILTER_LZMA2,  "lc": lc, "lp":lp, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
    LZMA2_HLP_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": 0, "lp":4, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]
    LZMA2_HLC_filter = [
            {"id": lzma.FILTER_LZMA2,  "lc": 4, "lp":0, "pb":pb , "mode":mode,  "mf":mf,\
             "nice_len": nice_len, "dict_size": dict_size, "depth":depth}
        ]

    if compressionMethod == 0:
        #zip, no compression
        compressionMethod = '.zip'
        compressedName = (fileName + compressionMethod)
        with zipfile.ZipFile(compressedName,'w',zipfile.ZIP_STORED) as newFile:
            newFile.write(fileName)
            newFile.close()
    #zip deflate
    if compressionMethod == 1:
        compressionMethod = '.zip'
        compressedName = (fileName + compressionMethod)
        with zipfile.ZipFile( compressedName,'w',zipfile.ZIP_DEFLATED) as newFile:
            newFile.write(fileName)
            newFile.close()

    #bzip
    if compressionMethod == 2:
        compressionMethod = '.bz'
        compressedName = (fileName + compressionMethod)
        with bz2.BZ2File( compressedName,'w') as newFile:
            newFile.write(testFile.read())
            newFile.close()





     #lzma modes

    #std lzma2
    if compressionMethod == 3:
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open( compressedName,'wb', filters=std_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()



    #std lzma 1
    if compressionMethod == 4:
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(compressedName,'wb',filters=std_LZMA1_filter, format=lzma.FORMAT_ALONE)
        newFile.write(testFile.read())
        newFile.close()


        #delta LZMA2
    if compressionMethod == 5:
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_DELTA1_filter)
        newFile.write(testFile.read())
        newFile.close()


    #HLP lzma
    if compressionMethod == 6:
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_HLP_filter)
        newFile.write(testFile.read())
        newFile.close()


    #HLC lzma
    if compressionMethod == 7:
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_HLC_filter)
        newFile.write(testFile.read())
        newFile.close()



     #HPB lzma
    if compressionMethod == 8:
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(compressedName,'wb',filters=LZMA2_HPB_filter)
        newFile.write(testFile.read())
        newFile.close()




    #ARM lzma
    if compressionMethod == 9:
        BJC = lzma.FILTER_ARM
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)

        newFile = lzma.open(compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()


    #FILTER_ARMTHUMB lzma
    if compressionMethod == 10:
        BJC = lzma.FILTER_ARMTHUMB
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()



    #IA64 lzma
    if compressionMethod == 11:
        BJC = lzma.FILTER_IA64
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(  compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()


    #POWERPC lzma
    if compressionMethod == 12:
        BJC = lzma.FILTER_POWERPC
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(  compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()

    #SPARC lzma
    if compressionMethod == 13:
        BJC = lzma.FILTER_SPARC
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)
        newFile = lzma.open(compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()


    #X86 lzma
    if compressionMethod == 14:
        BJC = lzma.FILTER_X86
        BJC_LZMA2_filter[0].update({"id":BJC})
        compressionMethod = '.lzma'
        compressedName = (fileName + compressionMethod)


        newFile = lzma.open(  compressedName,'wb',filters=BJC_LZMA2_filter)
        newFile.write(testFile.read())
        newFile.close()



        #GZIP
    if compressionMethod == 15:
        compressionMethod = '.gz'
        compressedName = (fileName + compressionMethod)
        newFile = gzip.open(compressedName,'w')
        newFile.write(testFile.read())
        newFile.close()

        #zlib
    if compressionMethod == 16:
        compressionMethod = '.gzip'
        compressedName = (fileName + compressionMethod)
        newFile = open(   compressedName,'w')
        compressedContent = zlib.compress(testFile.read(),9)
        newFile.write(compressedContent)
        newFile.close()

