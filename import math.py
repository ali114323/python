import math

pi = math.pi

def areaofcircle():
    area = (str(pi * r ** 2))
    return(area)

a = input("Do you want to find the area of a circle or a square? ")
if (a == "square"):
    print("We're calculating the area of a square! ")
    l = int(input("Whats your length? (No cm) "))
    h = int(input("Whats your height? (No cm) "))
    d = l * h
    print("Your area is:")
    print(d)
if (a == "circle"):
    print("We're calculating the area of a cirlce! ")
    r = int(input("What's your radius? (No cm) "))
    print("You're area is " + areaofcircle())

input("Press here to exit...")