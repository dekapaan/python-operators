# Task1
x = float(input("Enter first side of triangle: "))
y = float(input("Enter second side of triangle: "))
z = ((x**2) + (y**2))**(1/2)
print("Third side of triangle is", z)
print("")

h = float(input("What is the base of the triangle? "))
b = float(input("What is the base of the triangle? "))
area = int((h*b)/2)
print("Area of triangle is", bin(area))

# Task2
my_numbers = [2, 56, 12, 67, 1000, 32, 89, 29, 44, 39, 200, 11, 21]
a = max(my_numbers)
print(a)
b = min(my_numbers)
print(b)
