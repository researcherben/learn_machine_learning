'''
Is the weather good?
Does your boyfriend or girlfriend want to accompany you?
Is the festival near public transit? (You don't own a car).

We can represent these three factors by corresponding binary 
variables x1, x2 and x3. For instance, we'd have x1=1 if the 
weather is good, and x1=0 if the weather is bad. Similarly, 
x2=1 if your boyfriend or girlfriend wants to go, and x2=0 
if not. And similarly again for x3 and public transit.
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


# input decision factors; value 0 or 1
#    weather  friend    transit
#    good=1   go    =1  near=1
#    bad =0   not go=0  far =0
x = [1,       0,        0]

# weight. Higher value means more important
w = [6,       2,        2]

threshold = 5

reslt = dot_product(x,w)
if ( reslt <= threshold ):
  output=0
  print("don't go to cheese festival")
else: # reslt > threshold
  output=1
  print("go to cheese festival")
