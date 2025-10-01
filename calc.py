def do(a,b,o):
    if o=="+":
        return a+b
    if o=="-":
        return a-b
    if o=="x":
        return a*b
    if o=="/":
        if b==0:
            print("error - cannot divide by 0") 
            return 0
        return a/b
    else:
        print("error - input not acceptable") 
        return
print("CALCULATOR") 
x=input("Value 1: ")
y=input("Value 2: ")
z=input("Operation (+,-,x,/): ")
print("Result:",do(int(x),int(y),z))
