'''
half-adder
http://www.egr.msu.edu/classes/ece410/mason/files/Ch12.pdf
x1 x2 sum carry
0  0  0   0
0  1  1   0
1  0  1   0
1  1  0   1

NAND
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

# input; value 0 or 1
for indx in range(4):
  if   (indx == 0): x = [ 0,  0]
  elif (indx == 1): x = [ 1,  0]
  elif (indx == 2): x = [ 0,  1]
  elif (indx == 3): x = [ 1,  1]
  else: print("error in indx")
  
  print("input: "+str(x[0])+", "+str(x[1])+"; output from NAND gates")
  a = nand(x)
  sum_vec1=nand([x[0],a])
  sum_vec2=nand([x[1],a])
  print("sum:   "+str(nand([sum_vec1,sum_vec2])))
  print("carry: "+str(nand([a,a])))

  print("input: "+str(x[0])+", "+str(x[1])+"; output from perceptrons")
  weight_vec=[-2, -2]
  bias=3
  a = perceptron(x, weight_vec, bias)
  m = perceptron([x[0], a], weight_vec, bias)
  n = perceptron([x[1], a], weight_vec, bias)
  print("sum:   "+str(perceptron([m, n], weight_vec, bias)))
  print("carry: "+str(perceptron([a, a], weight_vec, bias)))
  print(" ")
