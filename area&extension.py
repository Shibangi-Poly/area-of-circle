# gives the area of the circle as per the radius given by the user
PI = 3.14
a = float(input('Please enter the radius of a circle: '))
area = PI*a*a
print("Area of the circle is: ",area)
# gives the extension of the file entered by the user
filename = input("Enter the filename: ")
f_extension = filename.split(".")
print("The extension of the file is: "+ repr(f_extension[-1]))
