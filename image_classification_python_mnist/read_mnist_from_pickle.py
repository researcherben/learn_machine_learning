# http://deeplearning.net/tutorial/gettingstarted.html
# http://deeplearning.net/data/mnist/mnist.pkl.gz

import cPickle, gzip, numpy

# Load the dataset
f = gzip.open('data_files_pickled/mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()

