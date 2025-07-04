def sub(a:int,b:int):
    return a+b
def subtract(a:int,b:int):
    return a-b
def multiply(a:int,b:int):
    return a*b
def dvide(a:int,b:int):
    return a/b
def main():
    a=int(input(""))
    b=int(input(""))
    os=input(" + , - , / , * ")
    if os=="+":
        print(sub(a,b))
    elif os=="-":
        print(subtract(a,b))
    elif os=="*":
        print(multiply(a,b))
    elif os=="/":
        print(dvide(a,b))
    else:
        print("Faqat arfimetik ammalar kiriting?")
print(main())