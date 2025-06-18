# we are converting our user input from string to float, 2 reasons
# 1. So we can input numbers like 9.75 in the terminal
# 2. So the can be used to calculate the area in the area variable
# otherwise we get this error: TypeError: can't multiply sequence by non-int of type 'str'
length = float(input("Input the LENGTH of the rectangle: "))
width = float(input("Input the WIDTH of the rectangle: "))

area = length * width

print(f"The area is {area} cm^2")