# if_triangle Day 3 AoC Python

import numpy as np

#a=3
#b=4
#c=5

filepath='AoC_Day3_directions'
triangle_list=open(filepath,'r')

triangle_array=np.genfromtxt(filepath,delimiter="",names=['a','b','c'])

def is_triangle(a,b,c):
  if (a>b+c) or (b>a+c) or (c>a+b):
    return 0
  elif c==a+b or b==a+c or a==b+c:
    return 0
  else:
    return 1
  
#print(is_triangle(a,b,c))
print('a',int(triangle_array[8]['a']))
print('b',int(triangle_array[8]['b']))
print('c',int(triangle_array[8]['c']))

#print(range(len(list(triangle_array))))
#print('Length of array',list(range(len(triangle_array))))
counter=0

#counter=is_triangle(a,b,c)

for row in list(range(len(triangle_array))):
  counter+=is_triangle(int(triangle_array[row]['a']),
		       int(triangle_array[row]['b']),
		       int(triangle_array[row]['c']))
  #print(counter)
print(counter)