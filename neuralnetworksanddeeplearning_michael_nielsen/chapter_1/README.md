git clone https://github.com/mnielsen/neural-networks-and-deep-learning.git
cd neural-networks-and-deep-learning/src
python

>>> import mnist_loader
>>> training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
>>> import network
>>> net = network.Network([784, 30, 10])
>>> net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
Epoch 0: 8260 / 10000
Epoch 1: 8397 / 10000
Epoch 2: 8460 / 10000
Epoch 3: 8512 / 10000
Epoch 4: 8512 / 10000
Epoch 5: 8542 / 10000
Epoch 6: 8558 / 10000
Epoch 7: 8556 / 10000
Epoch 8: 8558 / 10000
Epoch 9: 8585 / 10000
Epoch 10: 8602 / 10000
Epoch 11: 8566 / 10000
Epoch 12: 9416 / 10000
Epoch 13: 9457 / 10000
Epoch 14: 9476 / 10000
Epoch 15: 9471 / 10000
Epoch 16: 9489 / 10000
Epoch 17: 9475 / 10000
Epoch 18: 9482 / 10000
Epoch 19: 9510 / 10000
Epoch 20: 9480 / 10000
Epoch 21: 9522 / 10000
Epoch 22: 9492 / 10000
Epoch 23: 9519 / 10000
Epoch 24: 9496 / 10000
Epoch 25: 9527 / 10000
Epoch 26: 9491 / 10000
Epoch 27: 9484 / 10000
Epoch 28: 9515 / 10000
Epoch 29: 9532 / 10000

