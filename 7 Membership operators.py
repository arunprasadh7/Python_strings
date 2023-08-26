# Membership operators in strings - in, not in

# in operator

s = 'arun'

s1 = 'a' in 'arun'
print(s1)

s2 = 'z' in 'arun'
print(s2)

s3 = 'z' not in 'arun'
print(s3)

#eg prb

s = input('Enter main string: ')
s1 = input('Enter sub-string: ')

if s1 in s:
  print(f'{s1} present in {s}.')

else:
  print(f'{s1} not present in {s}.')