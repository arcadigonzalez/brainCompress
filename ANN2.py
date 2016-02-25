from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.tools.customxml import NetworkWriter
from pybrain.tools.customxml import NetworkReader
import pybrain
import dataset2
from pybrain.supervised.trainers import BackpropTrainer
import time


data = dataset2.genTestDataset2()
theNet = FeedForwardNetwork()

bitsPerByte = 8;
bytesToAnalize = 128;
numberOfOutputs = 17

inLayer = []
hiddenLayer1 = []
hiddenLayer2 = SigmoidLayer(bytesToAnalize, name='hidden2')
outLayer = LinearLayer(numberOfOutputs, name = 'output')

in_to_hidden = []
hidden1_to_hidden2 = []
theNet.addModule(hiddenLayer2)

for i in range(0,bytesToAnalize):
    inLayer.append(LinearLayer(bitsPerByte, name=("bit " + str(i*8) + " to " +str(i*8+bitsPerByte))))
    hiddenLayer1.append(SigmoidLayer(1, name = ("byte " + str(i))))
    in_to_hidden.append(pybrain.structure.FullConnection(inLayer[i],hiddenLayer1[i], name =("connection "+ str(i+1) + " of 128")))
    theNet.addInputModule(inLayer[i])
    theNet.addModule(hiddenLayer1[i])
    theNet.addConnection(in_to_hidden[i])
    hidden1_to_hidden2.append(pybrain.structure.FullConnection(hiddenLayer1[i],hiddenLayer2, name= ("byte " + str(i) + " to hidden2")))
    theNet.addConnection(hidden1_to_hidden2[i])





theNet.addOutputModule(outLayer)

theNet.sortModules()


hidden_to_out = pybrain.structure.FullConnection(hiddenLayer2,outLayer, name = 'hidden to output')

theNet.addConnection(hidden_to_out)

theNet.sortModules()
inp = data['input']
oup = data['target']
print(inp[2,:])
print(oup[2,:])


testData, trainData = data.splitWithProportion(0.2)
trainer = BackpropTrainer(theNet, trainData, verbose=True)
for i in range(2500):
    print ("epoch " + str(i))
    trainer.trainEpochs( 1 )
    if i%20 == 0:
        NetworkWriter.writeToFile(theNet,"/Users/arcadigonzalez/PycharmProjects/anncomp_pro/ANN2_Backups/"+str(i))
        NetworkWriter.writeToFile(theNet,"/Users/arcadigonzalez/Google Drive/NN_BU/NN2/"+str(i))
        print("resting processor, writing file")
        time.sleep(120)

