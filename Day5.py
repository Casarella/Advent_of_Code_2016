# Day 5 AoC

import collections as col
import numpy as np
import re
import hashlib as hh

#password='abc3231929'
#password='abc5017308'
#password='abc5278568'
password='wtnhxymk'

#md5=hh.md5(password.encode()).hexdigest()
md5=0

def find_md5():
  """
  Returns the md5 hashes where the first five digits are 0
  """
  md5_test=hh.md5((password+str(number)).encode()).hexdigest()
  if md5_test[0:5]=='00000':
    return True
  else:
    return False

def cinco0_md5():
  return hh.md5((password+str(number)).encode()).hexdigest()
#print(md5)
correct_md5_00000=[]

def password_digit():
  """
  Returns the 6th digit of the MD5 hash when the code requirements
  are met (first five digits are 0)
  """
  return cinco0_md5()[5] 
N=10000000
for number in range(N):
  if find_md5()==True:
    correct_md5_00000.append(password_digit())
  #print(password_digit())

print(correct_md5_00000)
#print(password_digit())