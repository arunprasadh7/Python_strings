#accessing string using slice operator
# we can get a substring using slice
# index we can get single char , slice provides range of chars or substring
#Syntax: s[bEginindex:endindex:step]

s = 'abcdefghij'

print(s[2:7]) #from 2 to 6 (n-1)
print(s[:7])  #0 to 6(7-1)
print(s[2:])  #2 till end
print(s[:])  #from start to end, entire string


#introducing step with slicing

print(s[2:7:1]) #step 1-default
print(s[2:7:2]) #step of 2
print(s[2:7:3]) #step of 3
print(s[2:7:-1]) #step of -1 in reverse
print(s[::-1]) #entire string in reverse
print(s[::-2]) #entire string in reverse in steps 2
