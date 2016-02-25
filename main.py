import pybrain
from pybrain.tools.customxml import NetworkReader
from compressionFN import compressSingle
bitsToAnalise = 128*8

def bits(f):
    bytes = (ord(b) for b in f.read())
    for b in bytes:
        for i in xrange(8):
            yield (b >> i) & 1

ratiosNetwork = pybrain.FeedForwardNetwork()
ratiosNetwork = NetworkReader.readFrom('/Users/arcadigonzalez/PycharmProjects/anncomp_pro/ANN_Backups/2480')
bestNetwork = pybrain.FeedForwardNetwork()
bestNetwork = NetworkReader.readFrom('/Users/arcadigonzalez/PycharmProjects/anncomp_pro/ANN2_Backups/2480')

algorithms = ['ZIP, no compression', 'ZIP and DEFLATE','BZip', 'LZMA2', 'LZMA1','delta and LZMA', 'LZMA2 with high literal context bits', 'LZMA with high literal position bits'\
              ,'LZMA with high position bits', 'LZMA with ARM architechture BCJ','LZMA with ARM Thumb architechture BCJ','LZMA with IA64 architechture BCJ', \
              'LZMA with IBM PowerPC architechture BCJ','LZMA with Oracle SPARC architechture BCJ','LZMA with Intel x64-86 architechture BCJ','GZip','Zlib']

exitval = 0
while exitval < 1:
    file = raw_input("enter full path to file: ")
    bitsArr = []

    i = 0
    #generate array of bits to feed the network
    for b in bits(open(file)):
        if i < bitsToAnalise:
             bitsArr.append(b)
             i+=1
        else:
            break
    if bitsArr.__len__()<bitsToAnalise:
                    for i in range(bitsArr.__len__(), bitsToAnalise):
                        bitsArr.append(0)

    ratiosArr = (ratiosNetwork.activate(bitsArr))
    bestArr = (bestNetwork.activate(bitsArr))

    bestAlgo = 0
    for n in range (0, bestArr.__len__()):
        if bestArr[bestAlgo]>bestArr[n]:
            bestAlgo = n

    print(algorithms[bestAlgo]+ " will obtain a compression ratio of around: " + str(ratiosArr[bestAlgo]))

    nb = raw_input("compress? (y/n) ")
    if nb == "y":
        compressSingle(file,bestAlgo)
        print("compression done")

    nb = raw_input("Exit? (y/n) ")
    if nb == "y":
        exitval = 1
        exit()
