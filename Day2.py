# Advent of Code Day 2

# Keypad is 3x3 square, directions are in file 
# "AoC_Day2_directions" - U goes up one key (ignoring 
# subsequent retrievals for a direction at the edge)

# Ignoring of commands occurs in two places, where there are >2 
# subsequent commands in the same direction OR when you reach an 
# edge of the grid and try to keep moving OFF the grid

import numpy as np
import re

directions_path='AoC_Day2_directions'
#directions_list=[]
U = np.array([0,1])
R = np.array([1,0])
D = np.array([0,-1])
L = np.array([-1,0])
C = np.array([0,0])

direction_dict={'U':U,'R':R,'D':D,'L':L,'\n': C}
print(direction_dict)

#directions_list=list(list(open(directions_path,'r'))[2])


#print(directions_list)

key0=[0,0]

# Imagine this is simply a grid, with 
# U adding [0,1]
# R adding [1,0]
# D adding [0,-1]
# L adding [-1,0]



# Clip directions at edge
#key_vector=[]
key_vector=np.array([0,0])
def take_step():
  return direction_dict[entry]

#for entry in directions_list:
#for entry in directions_list:
  #take_step()
  #print('step',key_vector)
  

def normalize_edge():
  """
  After each 'step', check to see if the vector coordinates are >+/-1, if 
  they are, just change them to +/-1
  """
  if key_vector[0]>1:
    key_vector[0]=1
  elif key_vector[0]<-1:
    key_vector[0]=-1
  elif key_vector[1]>1:
    key_vector[1]=1
  elif key_vector[1]<-1:
    key_vector[1]=-1    
  return key_vector


# Define final button press after directions
def button_press():
  if np.array_equal(key_vector,U+L):
    return '1'
  elif np.array_equal(key_vector,U):
    return '2'
  elif np.array_equal(key_vector,U+R):
    return '3'
  elif np.array_equal(key_vector,L):
    return '4'
  elif np.array_equal(key_vector,C):
    return '5'
  elif np.array_equal(key_vector,R):
    return '6'
  elif np.array_equal(key_vector,D+L):
    return '7'
  elif np.array_equal(key_vector,D):
    return '8'
  else:
    return '9'

#test section
#key_vector=key0+direction_dict['L']
#print(key_vector)
#key_vector+=direction_dict['L']
#print(key_vector)
#normalize_edge()
#print(key_vector)
#print('Button press:',button_press())

# order of operations:
# step, normalize, step until end, return button press
for key_number in range(len(list(open(directions_path,'r')))):
  directions_list=list(list(open(directions_path,'r'))[key_number])
  for entry in directions_list:
    key_vector+=take_step()
    normalize_edge()
  #print('Move:',key_vector)
  print(button_press())