from pybrain.datasets import SupervisedDataSet
import pickle
import os

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def genTestDataset2():
    filenum = 0;
    megaArrStats = []
    megaArrBits = []
    grandPaDir = '/training'

    inputs = 128*8
    outputs = 17
    dataset = SupervisedDataSet(inputs, outputs)

    cwd = "/stats/"
    for file in os.listdir(cwd):
        if file == ".DS_Store":
            filenum+=1
            continue
        if filenum%4 == 0:
            megaArrStats.append(pickle.load(open(os.getcwd()+ "/stats/"+file, 'r')))
            filenum +=1
            continue
        if filenum%4 == 2:
            megaArrBits.append(pickle.load(open(os.getcwd()+ "/stats/"+file, 'r')))
            filenum+=1
            continue
        filenum+=1

    kiloArrBits = []
    kiloArrStats = []
    arrBits = []
    arrStats = []
    miliArrBits = []
    miliArrStats = []
    compareArrStats = []

    assert megaArrBits.__len__() == megaArrStats.__len__()
    for i in range(0,megaArrStats.__len__()):
        kiloArrBits = megaArrBits[i]
        kiloArrStats = megaArrStats[i]
        assert kiloArrStats.__len__() == kiloArrBits.__len__()
        for j in range (0,kiloArrStats.__len__()):
            arrBits = kiloArrBits[j]
            arrStats = kiloArrStats[j]
            assert arrBits[0] == arrStats[0]
            #print arrBits[0]
            #print arrStats[0]
            for k in range(1,arrBits.__len__()):
                miliArrBits.append(arrBits[k])
            for l in range(1,arrStats.__len__()-4,4):
                miliArrStats.append(float(arrStats[3+l]))
                #print(miliArrStats)
            if miliArrBits.__len__()<inputs:
                for i in range(miliArrBits.__len__(), inputs):
                    miliArrBits.append(0)
            compareArrStats = list(miliArrStats)
            bubbleSort(compareArrStats)
            for m in range (0,compareArrStats.__len__()):
                for n in range(0, miliArrStats.__len__()):
                    if compareArrStats[m] == miliArrStats[n]:
                        miliArrStats[n] =m


            dataset.addSample(miliArrBits,miliArrStats)
            miliArrBits = []
            miliArrStats = []


    return dataset

