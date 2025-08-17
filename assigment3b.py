import math


num = float(input("Enter a number: "))

sqrt_val = math.sqrt(num)
log_val = math.log(num)   # natural log (base e)
sine_val = math.sin(num)  # sine expects radians

print("Square root of", num, "is:", sqrt_val)
print("Natural logarithm of", num, "is:", log_val)
print("Sine of", num, "is:", sine_val)
