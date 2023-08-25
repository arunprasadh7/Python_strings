#how to access chars of string and application
#there are 2 ways of accessing strings in python
#indexing & slicing

#using index: supports both +ve and -ve index
s = 'arun'
print(s[0])
print(s[-1])

#If we are trying to access characters of a string with out of range index then we will get error saying: IndexError

'''Write a Program to Accept some String from the Keyboard and display its
Characters by Index wise (both Positive and Negative Index)'''

s = input('Enter a string : ')
i = 0
for x in s:
  print(f'The +ve index is {i}, -ve index is {i-len(s)} and the character is {x}.')
