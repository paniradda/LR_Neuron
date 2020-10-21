Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.chdir ('')
KeyboardInterrupt
>>> os.chdir ('C:\\Users\\Radda\\Desktop\\Python_Radda\\Neuron\\NeuralNetwork')
>>> import mnist_loader
>>> training_data, validation_data, test_data =
mnist_loader.load_data_wrapper()
SyntaxError: invalid syntax
>>> training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
>>> import network
Сеть net:
Количетво слоев: 3
Количество нейронов в слое 0 : 2
Количество нейронов в слое 1 : 3
Количество нейронов в слое 2 : 1
W_ 1 :
[[-0.45  0.4 ]
 [ 1.06  3.04]
 [ 0.61 -0.47]]
b_ 1 :
[[-0.08]
 [ 1.17]
 [-1.59]]
W_ 2 :
[[ 1.16 -1.13  0.09]]
b_ 2 :
[[0.65]]
>>> net = network.Network([784, 30, 10])
>>> net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
Epoch 0: 9000 / 10000
Epoch 1: 9259 / 10000
Epoch 2: 9302 / 10000
Epoch 3: 9317 / 10000
Epoch 4: 9380 / 10000
Epoch 5: 9364 / 10000
Epoch 6: 9431 / 10000
Epoch 7: 9391 / 10000
Epoch 8: 9457 / 10000
Epoch 9: 9451 / 10000
Epoch 10: 9438 / 10000
Epoch 11: 9412 / 10000
Epoch 12: 9482 / 10000
Epoch 13: 9476 / 10000
Epoch 14: 9508 / 10000
Epoch 15: 9492 / 10000
Epoch 16: 9496 / 10000
Epoch 17: 9486 / 10000
Epoch 18: 9497 / 10000
Epoch 19: 9493 / 10000
Epoch 20: 9482 / 10000
Epoch 21: 9480 / 10000
Epoch 22: 9486 / 10000
Epoch 23: 9500 / 10000
Epoch 24: 9508 / 10000
Epoch 25: 9488 / 10000
Epoch 26: 9500 / 10000
Epoch 27: 9495 / 10000
Epoch 28: 9517 / 10000
Epoch 29: 9495 / 10000
>>> 
