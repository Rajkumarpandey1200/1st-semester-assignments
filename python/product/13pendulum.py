# To determine the acceleration due to gravity on the basis of the
# effective length of a simple pendulum.
# g=4π**2L/t**2

import math

length=float(input("enter length of a pendulum (in meter):"))
time=float(input("Enter period of 1 Oscillation(in seconds) :"))

gravity_acceleration= 4* math.pi**2 *length/time**2
print("' the acceleration due to gravity on the basis of the\
 effective length of a simple pendulum:",round(gravity_acceleration,2))
