#Day 6 AoC

import collections as col
import numpy as np
import re
import operator

filepath='AoC_Day6_directions'


signal=list(open(filepath,'r'))
signal_array=np.array(signal)
split_signal=[]
for row in list(range(len(signal_array))):
  split_signal.append(list(signal_array[row]))

#print(split_signal)

#for row in signal_array:
  #for entry in list(range(8)):
    #split_signal.append(re.findall(r"[\w+]",signal_array[entry]))

print(np.array(split_signal).shape)
#print(re.findall(r"[\w+]",signal_array[0]))
transpose_signal=(np.transpose(np.array(split_signal)))


#print(split_signal)
#print(transpose_signal)

for row in list(range(len(transpose_signal))):
  print((col.Counter(transpose_signal[row]).most_common()))


#counter_dict=dict((entry,transpose_signal[0].count(entry)) for entry in transpose_signal[0])  
#print(counter_dict)