# Day 4 Advent of Coding


import numpy as np
import re
import collections as col
import operator

filepath='AoC_Day4_directions'
names_list=list(open(filepath,'r'))
#print(list(open(filepath,'r')))
#avwqbizmxwzmewtnmdqawzzwk
#encrypted_name='kwzzwaqdm-ntwemz-wxmzibqwva-434[nwzml]'

encrypted_name=[]

def checksum():
  """
  Returns the checksum for the room to determine realness
  """
  return encrypted_name[-7:-2]

def sector_ID():
  """
  Returns the sector ID, for use only if the room is 'real'
  """
  return encrypted_name[-10:-7]

def room_code():
  """
  removes '-' marks and returns a string of the letters ready 
  to count with Counter
  """
  return re.sub('-','',encrypted_name[-11::-1])

#test section

#code=re.sub('-','',room_code())
#code=re.search(r"\w+",room_code()).group()
#print(code)

#print('checksum -',checksum())
#print('Sector ID -',sector_ID())
#print('Room code -',room_code())

#print(room_code())

#sorted(counts, key=lambda word: (-counts[word], word))

def most_common():
  #return col.Counter(room_code()).most_common(5)
  return sorted((col.Counter(room_code()).most_common(5)), key=operator.itemgetter(1))
#most_common=col.Counter(room_code()).most_common(5)
#print('Most common letters -',most_common)

#print(most_common())

def checksum_match():
  """
  Returns the 'calculated' checksum from the codename
  """
  return most_common()[0][0]+most_common()[1][0]+most_common()[2][0]+most_common()[3][0]+most_common()[4][0]
    

#print('counted checksum -',checksum_match())

def is_real_room():
  if checksum_match()==checksum():
    return sector_ID()
  else:
    return 0
  
#print('Real room? ',is_real_room())

for row in list(range(len(names_list))):
  encrypted_name=names_list[row]
  print(checksum_match()[::-1])
  #print(sorted(most_common(),key=operator.itemgetter(0)))
  #print('Actual checksum','Calc Checksum')
  #print(checksum(),'=',checksum_match(),'?')
  #print(is_real_room())
  #print(room_code())
  #counter+=is_real_room()

#print(counter)