#Finding substrings using find() rfind()

'''
s.find(substring)
Returns index of first occurrence of the given substring. If it is not available then we will
get -1.
'''

s="Learning Python is very easy"
print(s.find("Python")) #9
print(s.find("Java")) # -1
print(s.find("r"))#3
print(s.rfind("r"))#21 

#By default find() method can search total string. We can also specify the boundaries to search.
# s.find(substring,bEgin,end)

s="durgaravipavanshiva"
print(s.find('a'))#4
print(s.find('a',7,15))#10
print(s.find('z',7,15))#-1 

