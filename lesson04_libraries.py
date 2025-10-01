#  librarys

import math

print("\n-------------------MATH-------------------\n")

print("square root: \t", math.sqrt(25))
print("round up: \t", math.ceil(4.2))
print("round down: \t", math.floor(4.8))
print("power: \t", math.pow(2, 5))
print("pi: \t", math.pi)

# ranodm library
# uses Psudeorandom generator(PRNG)
# NOT true random
# uses an complex algoritim  that is predictable but good enough for most use cases


seed = 54.875

step1 = seed * 4
step2 = seed + step1 ** 2
step3 = step2 / 10000
step4 = step3 - math.floor(step3)

print(math.floor(step4 * 10))


import random

print("Random integer: ", random.randint(1, 7))
print(random.random())

my_favs = ["taco", "burrito", "enchilada", "quesadilla"]
print(random.choice(my_favs)) 


# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2
diameter = 14

r = diameter/2
pi = math.pi
circle = pi*r**2
print(circle)


# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

die_roll = random.choice(["1", "2", "3", "4", "5", "6"])
print(die_roll)