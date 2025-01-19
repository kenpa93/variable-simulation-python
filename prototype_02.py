#Module to be imported for delay function of python
import time
from math import *
#Instructions for users
print("Which equation you wanna test in this simulation")
time.sleep(0.5)
#Equation example for user
print("Equation int the background like a+b=c, a-b=c")
#delay module by python you can use it to create a delay between two functions
time.sleep(0.5)
print("WARNING:-This simulation is under development")
time.sleep(0.5)
print("This simulation can only find the values of the basic equations")
time.sleep(0.5)
print("!.Add")
time.sleep(0.5)
print("2.Subtract")
time.sleep(0.5)
print("3.Multiply")
time.sleep(0.5)
print("4.Divide")
time.sleep(0.5)
print("5.finding sqaure of the answer")
print("for example x^2=49 and you wanna know the value of x")
time.sleep(0.5)
print("6.finding the value inside the squareroot of the answer")
print("for example √x = 7 and you wanna know the value of x")
time.sleep(0.5)
a=int(input("Which equation wanna try my master(write number of the choice) "))
#Main Logistics Algorithms
if(a==1):
    d=0
    c=int(input("please enter the answer you want to expect from me "))
    e=int(input("Enter the value you want to be fixed with the answer "))
    while d+e !=c:
        d+=1        
        if(d+e==c):
            print("Success the first value is ")
            print(d)
            print("The second value is ")
            print(e)
            break
elif(a==2):
    c=int(input("Please enter the answer you expect from me "))
    e=int(input("Please enter the fixed value of your equation "))
    d=0
    while d-e !=c:
        d+=1
        if(d-e==c):
            print("Sucess the other value is ")
            print(d)
            print("The fixed number you entered is this")
            print(e)
            break
elif(a==3):
    c=int(input("Please enter the answer you expect from me "))
    e=int(input("Please enter the fixed value of your equation "))
    d=1
    f=0
    while f != c:
        d+=1
        f=d*e
        if(f==c):
            print("Sucess the other value is ")
            print(d)
            print("The fixed number you entered is this")
            print(e)
            break
        elif f > c:
            print("No integer solution: 'e' cannot be found such that 'd * e' equals 'c'.")
            break
elif(a==4):
    c=int(input("Please enter the answer you expect from me "))
    e=int(input("Please enter the fixed value of your equation "))
    d=0
    while d/e !=c:
        d+=1
        f=d/e
        if(d/e==c):
            print("Sucess the other value is ")
            print(d)
            print("The fixed number you entered is this")
            print(e)
            break
        elif f > c:
            print("No integer solution: 'e' cannot be found such that 'd * e' equals 'c'.")
            break
elif(a==5):
    c=int(input("Please enter the answer "))
    d=sqrt(c)
    print("The answer is")
    print(d)
elif(a==6):
    c=int(input("Please enter the answer "))
    d=c**2
    print("The answer is")
    print(d)
else:
    print("Please write the number of the above choices")