#Day 7 AoC Python3.4

import re

filepath='AoC_Day7_directions'

IPv7=open(filepath,'r')
test_line='vjqhodfzrrqjshbhx[lezezbbswydnjnz]ejcflwytgzvyigz[hjdilpgdyzfkloa]mxtkrysovvotkuyekba'
#print(IPv7.readlines()[6])

def is_ABBA():
  """
  Returns True if a string section is a palindrome of ABBA type
  (inner characters are distinctly different)
  """
  if string_query()[::-1]==string_query() and string_query()[0]!=string_query()[1]:
    return True
  else:
    return False
  
  
#print(is_ABBA())

def find_hypernet():
  """
  Find all instances of a hypernet address in the string
  """
  return re.findall('\[(.*?)\]',test_line) #change this to any line
hypernet_list=[]
def concat_hypernet(): # NEEDS WORK
  """
  Concatenates '[]'s to the hypernet for removal in the string
  """
  for entry in list(range(len(find_hypernet()))):
    return hypernet_list.append('['+find_hypernet()[entry]+']')

print(re.findall('\[(.*?)\]',test_line)) #this is the string inside the hypernet

#print(test_line.replace((re.findall('\[(.*?)\]',test_line)[entry] for entry in list(range(2))),""))

print(hypernet_list)
#print(test_line.replace(re.findall('\[(.*?)\]',test_line),'') )