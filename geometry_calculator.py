# using math functions
import math

print(f"Welcome to your Fun Math Calculator! 🧮")
print(f"Select an option:")
print(f"1. Calculate the circumference of a circle.")
print(f"2. Calculate the area of a circle.")
print(f"3. Calculate the Hypotenuse of a right triangle.")

choice = int(input("Enter 1, 2, or 3:"))

# Calculate the circumference of a circle.
if choice == 1:
    radius = float(input('Enter the radius of a circle: '))
    circumference = 2 * math.pi * radius
    print(f"The circumference of the circle is: {round(circumference,2)} cm")

# Calculate the area of a circle
elif choice == 2:
    radius = float(input('Enter the radius of a circle: '))
    area = math.pi * pow(radius, 2) #use pow function to raise our raidus to the power of 2
    print(f"The are of the circle is: {round(area, 2)}cm^2")

# Calculate the Hypotenuse of a right triangle - prompt the user for the lengths of side A and side B
elif choice == 3:
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    print(f"The hypotenuse is: {round(c,2)}")

else:
    print("Invalid option. Please select only 1, 2, or 3. ")