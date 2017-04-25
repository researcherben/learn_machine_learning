'''
Single perceptron can replicate a NAND gate

https://en.wikipedia.org/wiki/NAND_logic

inputs | output
0 0      1
0 1      1
1 0      1
1 1      0
'''

def dot_product(vec1,vec2):
  if (len(vec1) != len(vec2)):
    print("input vector lengths are not equal")
    print(len(vec1))
    print(len(vec2))
  reslt=0
  for indx in range(len(vec1)):
    reslt=reslt+vec1[indx]*vec2[indx]
  return reslt

def perceptron(input_binary_vector,weight_vector,bias):
  reslt = dot_product(input_binary_vector,weight_vector)
  if ( reslt + bias <= 0 ): # aka reslt <= threshold
    output=0
  else: # reslt > threshold, aka reslt + bias > 0
    output=1
  return output

def nand(input_binary_vector):
  if (len(input_binary_vector) != 2):
    print("input vector length is not 2; this is an NAND gate!")
  return int(not (input_binary_vector[0] and input_binary_vector[1]))

# weight. Higher value means more important
w = [-2, -2]
bias = 3

for indx in range(4):
  # input decision factors; value 0 or 1
  if   (indx == 0): x = [ 0,  0]
  elif (indx == 1): x = [ 1,  0]
  elif (indx == 2): x = [ 0,  1]
  elif (indx == 3): x = [ 1,  1]
  else: print("error in indx")

  print("input: "+str(x[0])+", "+str(x[1]))
  
  print("preceptron: "+str(perceptron(x,w,bias)))

  print("NAND:       "+str(nand(x)))

