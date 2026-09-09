def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=float(input("enter your 1 number....."))
b=float(input("enter your 2 number....."))
print("enter 1 for add......")
print("enter 2 for sub......")
print("enter 3 for mul......")
print("enter 4 for div......")
choice = input("")
if(choice=="1"):
    print(sum(a,b))
elif(choice=="2"):
    print(sub(a,b))
elif(choice=="3"):
    print(mul(a,b))
elif(choice=="4"):
     print(div(a,b))
else:
     print("invailid option")