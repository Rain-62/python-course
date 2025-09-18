
def add(x,y):
    
    return x+y

def sub(x,y):
    
    return x-y

def multiply(x,y):
    
    return x*y

def divide(x,y):
    if y == 0:
     return "Divison durch 0 geht nicht!"
    return x/y

statement = "ja"
while statement == "ja":

 print("Please enter your 2 numbers")
 x = float(input("x = "))
 y = float(input("y = "))

 print("Enter what you wanna do")

 funktion = input()
 if funktion == "add":
    print(add(x,y))
    
 elif funktion == "sub":
    print(sub(x,y))

 elif funktion == "multiply":
    print(multiply(x,y))

 elif funktion == "divide":
    print(divide(x,y))

 else:
    print("Didnt understand, try again!")
    
 statement = input("Nochmal?    ")

 if statement == "ja":
    print("ok du willst nochmal")

 if statement == "nein":
    print("ok schade, dann nicht")
    break

 
