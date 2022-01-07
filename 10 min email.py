import random
print('''Which type of e-mail you want?
        --> G-mail(g)
            OR
        --> Ramdom email(r)''')

value1="qwertyuiopasdfghjklzxcvbnm"
e1=random.choice(value1)
e2=random.choice(value1)
e3=random.choice(value1)
e4=random.choice(value1)
e5=random.choice(value1)
a=input()
if a=='r':
    print(e1+e2+e3+e4+e5+e1+e4+e2+"@"+e3+e4+e1+e5+e2+".com")

if a=='g':
    print(e1+e2+e3+e4+e5+e1+e4+e2+'@gmail.com')

else:
    print("Wrong input!!!")