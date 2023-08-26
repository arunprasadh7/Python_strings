#removing spaces from string strip(), lstrip(), rstrip()
'''
rstrip() - To remove spaces at right hand side
lstrip() - To remove spaces at left hand side
strip() - To remove spaces both sides
'''
name=input("Enter your  Name:").strip()
#sname=name.strip() #we can declared a sep variable or method chain as above

if name == 'Arun':
    print(f'Hello {name}.')
elif name == "Invoker":
    print(f'Hello {name}.')
elif name == 'Storm':
    print(f'Hello {name}.')
else:
    print('Name is invalid')