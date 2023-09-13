#index()
'''index() method is exactly same as find() method except that if the specified substring is not available then we will get ValueError.'''

s=input("Enter main string:")
subs=input("Enter sub string:") 
try:
    n = s.index(subs)
except ValueError:
    print('Substring not found.')

else:
    print('Substring found.')

