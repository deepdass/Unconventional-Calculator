

import math
b = None
print("""
>Calculator<
************************""")
def o():
    print("************************")
while True :
    try:
        b = input("""Type Quit to Quit
+,-,*,/,//,**,Root,Euler: """).lower()
        if b == "**":
            a = float(input('Number. '))
            c = float(input('power. '))
            e = a**c
            print("=",e)
            o()
        elif b == "+" or b == "-" or b == "*" or b == "/":
            a = input('First no. ')
            c = input('Second no. ')
            i = eval( a + b + c)
            print("= {:.2f}".format(i))
            o()
        elif b == "root":
             p = float(input("Number: "))
             print(math.sqrt(p))
        elif b == "euler":
             fa = int(input("Faces "))
             ve = int(input("Vertices "))
             ed= int(input("Edges "))
             tot = fa+ve-ed
             if tot == 2:
                  print("Possible")
             else:
                  print("Not Possible")
        elif b == "quit":
            print("Bye...")
            o()
            break
        else:
            print("I Don't Understand That ")
            o()
    except ValueError:
        print("Invalid Value")
        o()
    except ZeroDivisionError:
        print("Cannot Divide By Zero")
        o()
    except NameError:
        print("numbers only ")
        o()






##while True:
##    a = int(input("> "))
##    if a == 1 or a == 0:
##        print("Not a prime no.")
##    else: 
##        for pr in range(2,a):
##            if a%pr == 0:
##                print("Not a prime")
##                break
##        else:
##            print("Prime")
##
##
##
##
##
##
##
##a = int(input("number "))
##
##count = 1
##while count <= 10 :
##    b = a * count
##    print(a , "x" , count , "=" , b)
##    count+=1





