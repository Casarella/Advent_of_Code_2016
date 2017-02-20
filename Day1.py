#Advent of Code - Day 1 Solution

import numpy as np
import requests as rq

#data = rq.get("http://adventofcode.com/2016/day/1/input",auth=('crcasarella@gmail.com',''))
#print(data.text)

filepath='AoC_Day1_directions'
directions=[]
heading=90 #Sets the initial heading to North
with open(filepath, 'r') as f:
  #print(f.readlines())
  for entry in f.read().splitlines():
    directions.append(entry.split(","))
  
#print(directions)


#Reinvention of the wheel to occur:

turn_left = np.matrix([[0, -1], [1, 0]])
turn_right = np.matrix([[0, 1], [-1, 0]])

print(turn_left)

def travel_blocks():
  """
  Read the number of blocks to travel after turning a direction.
  """
  return int(entry[1:])

entry='L'
def read_turn():
  """
  Reads whether Santa needs to turn left or right from the list.
  """
  return entry[0]

def turn():
  """
  Performs the turn defined by read_turn().
  """
  if read_turn()=='R':
    return heading+-90
  elif read_turn()=='L':
    return heading+90
    
print(turn())