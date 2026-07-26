import math

print("==================")
print("Area Calculator")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

shape = int(input("Which shape: "))

if shape == 1:
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}")

elif shape == 2:
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    print(f"The area of the rectangle is {area}")

elif shape == 3:
    side = float(input("Side: "))
    area = side ** 2
    print(f"The area of the square is {area}")

elif shape == 4:
    radius = float(input("Radius: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is {area}")

elif shape == 5:
    print("Goodbye!")