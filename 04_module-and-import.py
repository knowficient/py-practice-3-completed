# Write a Python module for the 3 given equations below
import carfunc as fn

# BMW 3 Series
m = 2065   # Mass of car in kg
# Stationery
u = 0      # Initial velocity in kmph
v = 60     # Final velocity in kmph
ts = 7.2   # Time taken in seconds
# Moving at constant acceleration
d = 23.42  # Distance travelled in km
tm = 30/60 # Time taken in hours

print("The BMW 3 Series")

acc = fn.acceleration(u,v,ts)
print("The measured acceleration =", acc, "mps2")
force = fn.gforce(acc)
print("The measured G-force =", force, "g")
speed = fn.speed(d,tm)
print("Speed of car at constant acceleration =", speed, "kmph")
