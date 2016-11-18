# source: http://pjreddie.com/projects/mnist-in-csv/

def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16) # read 16 bytes of image file
    l.read(8)  # read 8  bytes of label file
    images = [] # initialize array

    for i in range(n): # loop over number of images
        image = [ord(l.read(1))]  # read 1 byte from label file; "ord" = Given a string of length one, return an integer
        for j in range(28*28): # image size is 28x28, j is pixel index in image
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte", "mnist_train.csv", 60000)
convert("t10k-images-idx3-ubyte",  "t10k-labels-idx1-ubyte",  "mnist_test.csv",  10000)

        
