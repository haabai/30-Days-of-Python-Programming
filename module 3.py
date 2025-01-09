# Declare your age as an integer variable
Age= 30

# Declare you height as a float variable
Height=5.8
# Declare a variable that store complex number
y=2 + 3j

# Write a script tha prompts the user to enter base and height of the triangle
base= int(input("Enter the base of the triangle: "))
height= int(input("Enter the height of the triangle: "))
# Calculate the area of the triangle
a=0.5*base*height
print(a)

# Write a script that prompts the user to enter side a, side b and side c of the triangle
a= int(input("Enter side a of the triangle: " ))
b= int(input("Enter side b of the triangle: " ))
c= int(input("Enter side c of the triangle: " ))
# Calculate the perimeter of the triangle
p= a+b+c
print(p)

# Get the length and width of a rectangle using prompts
length= int(input("Enter the length of the rectangle: " ))
width= int(input("Enter the width of the rectangle: " ))

# Calculate the area of the rectangle
length=10
width=7
area= length*width
print(f"The area of the rectangle is: {area}")
perimeter=2*(length*width)
print(f"The perimeter of the rectangle is: {perimeter}")

# Get area of a circle using prompt
Area= input("Enter the area of a circle:  ")
# Calculate the area of the circle
pi=3.14
r=7
print(f"the area of the circle is: {a}")
# Calculate the circumference of the circle
c=2*pi*r
r=7
print(f"The circumference of the circle is: {c}")

# Calculate the slope, x-intercept and y-intercept of y=2x-2
# y = 2x - 2
# Coefficients
m = 2  # slope
c = -2  # y-intercept
# Calculate x-intercept (y = 0)
x_intercept = -c / m
# Calculate y-intercept
y_intercept = c
print(f"Slope (m): {m}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

# Slope is (m=y2-y1/x2-x1). Find the slope and Euclidean distance between points (2,2) and points (6,10)
import math
# Coordinates of the points
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calculate the slope
slope = (y2 - y1) / (x2 - x1)
# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# Output the results
print(f"Slope (m): {slope}")
print(f"Euclidean distance (d): {distance:.2f}")

# Slope is (m=y2-y1/x2-x1). Find the slope and Euclidean distance between points (2,2) and points (6,10) in python
#Function to calculate slope
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return float('inf')  # Handle the case of vertical line
    return (y2 - y1) / (x2 - x1)
# Points for the first line
x1, y1 = 2, 2
x2, y2 = 6, 10
# Points for the second line
x3, y3 = 1, 0
x4, y4 = 0, -2
# Calculate the slopes
slope1 = calculate_slope(x1, y1, x2, y2)
slope2 = calculate_slope(x3, y3, x4, y4)
# Print the slopes
print(f"Slope of the first line: {slope1}")
print(f"Slope of the second line: {slope2}")
# Compare the slopes
if slope1 > slope2:
    print("The first line is steeper than the second line.")
elif slope1 < slope2:
    print("The second line is steeper than the first line.")
else:
    print("Both lines have the same slope.")

#calculate the value of y (y=x^2+6x+9). try to use different x values and figure out at what x value y is going to be 0 
# Define the function for the equation y = x^2 + 6x + 9
def calculate_y(x):
    return x**2 + 6*x + 9
# Test different x values
x_values = [-6, -3, 0, 3, 6,]
# Calculate and print y for each x value
for x in x_values:
    y = calculate_y(x)
    print(f"For x = {x}, y = {y}")
# Determine the x value where y is 0 by solving the quadratic equation
# y = x^2 + 6x + 9 can be factored as (x + 3)^2 = 0
import sympy as sp
# Define the variable and equation
x = sp.symbols('x')
equation = x**2 + 6*x + 9
# Solve the equation
solutions = sp.solve(equation, x)
print(f"The x value(s) where y = 0: {solutions}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
p= 'python'
d= 'dragon'
print(len(p))
print(len(d))
print(len('python') != len('dragon'))

# use an operator to check if 'on' is found in both 'python' and 'dragon'
result= 'on' in 'python' and 'on' in 'dragon'
print(result)

'i hope this course is not full of jargon'
# use in operator to check if jargon is in the sentence
sentence= 'i hope this course is not full of jargon'
result="jargon" in sentence
print(result)

# find the length of the text python and convert the value to float and string
Text= 'python'
# find the length]
length= len(Text)

# convert to float
length_as_float= float (length)

# convert to string
length_as_string= str(length)
print("Length:", length)
print("As float:", length_as_float)
print("As string:", length_as_string)

# How to check if a number is even or not using python
number= 8
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd")
    
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
result = 7 // 3
int_value= int(2.7)
if result == int_value:
    print("The floor division result is equal to the integer value of 2.7.")
else:
    print("The floor division result is not equal to the integer value of 2.7. ")

# Check if type of '10' is equal to type of 10
result = type('10') ==type(10)
print(result)
# Check if int('9.8') equal to (10)
result= int((float('9.8'))) == 10
print(result)

# write a script that prompts the user to enter hours and rate per hour.
hours= int(input("Enter hours worked: " ))
rate= int(input("Enter rate per hour: " ))
# Calculate pay of the person
weekly_earning= hours * rate
print(weekly_earning)

# Write a script that prompts the user to enter number of years.
years_lived= int(input("Enter the number of yerars lived: "))
# Calculate the number of seconds a person can live
# Define the average lifespan in years
years_lived = 100

# Calculate the number of seconds in a year (considering a common year with 365 days)
seconds_per_year = 365 * 24 * 60 * 60

# Calculate the total number of seconds for the average lifespan
total_seconds = years_lived * seconds_per_year

# Print the result
print(f"The number of seconds a person can live for {years_lived} years is approximately: {total_seconds} seconds")

# Write a python script that displays the following table
1,1,1,1,1
2,1,2,4,8
3,1,3,9,27
4,1,4,16,64
5,1,5,25,125
# Function to generate and display the table
def display_table():
    for i in range(1, 6):
        row = [i, 1, i, i**2, i**3]
        print(','.join(map(str, row)))

# Call the function to display the table
display_table()




# 








