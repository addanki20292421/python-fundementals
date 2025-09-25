# variable: holds a value stored in the physical storage on the computer and takes space
# Created by <vaiable name> = <Value as a datatype>

variable = 1
#^ variable^name
#          |
# vaiable value

variable2 = "variable 2"

# can be accessed by using the vriable name without quotes or anything

print("Variable: \t", variable)
print("Variable 2: \t", variable2, "\n")

print("Variable type: \t", type(variable))
print("Variable 2 type:  \t", type(variable2))

enabled = False
is_complete = True

print(is_complete)

# Variables can be overwritten
is_complete = False
print(is_complete)

# Variables should have meaningfull names even if its not required
a = "Blah Blah"
b = 5786342895


# Anybody looking at this has no idea what a and b are supposed to store
print(a)
print(b)


name = "Radia Pearlman"
age = 34
job = "Networking Engineer"


count = 10
count_but_added_5 = 15
print(count_but_added_5)

x = 4
y = "Hello"

temp = y
y=x
x=temp

print("X: \t", x)
print("Y: \t", y)
 
is_raining = False
is_raining = True
print("is it raining? \t", is_raining)