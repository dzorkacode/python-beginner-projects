def add(a,b):
    p=a+b
    return f"{a} + {b} = {p}"

def sub(a,b):
    s=a-b
    return f"{a} - {b} = {s}"

def mul(a,b):
    m=a*b
    return f"{a} - {b} = {m}"

def div(a,b):
    d=a/b
    return f"{a}/{b} = {d}"

while True:
    print("""A. ADDITION 
B. SUBTRACTION 
C. MULTIPLICATION 
D. DIVISION
E. EXIT""")
    choice=input("input your choice: ")

    if choice=='A' or choice=='a':
        print('ADDITION')
        a=int(input('input first number: '))
        b=int(input('input second number: '))
        print(add(a,b))
    elif choice=='B' or choice=='b':
        print('SUBTRACTION')
        a=int(input('input first number: '))
        b=int(input('input second number: '))
        print(sub(a,b))
    elif choice=='C' or choice=='c':
        print('MULTIPLICATION')
        a=int(input('input first number: '))
        b=int(input('input second number: '))
        print(mul(a,b))
    elif choice=='D' or choice=='d':
        print('DIVISION')
        a=int(input('input first number: '))
        b=int(input('input second number: '))
        if b==0:
            print('cannot divide by 0')
        else:
            print(div(a,b))
    elif choice=='E' or choice=='e':
        print('program ended')
    else:
        print("invalid input, try again")
        quit()