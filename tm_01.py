print("TAXI FARE CALCULATOR")
a = float(input("Enter begining odometer reading => "))
b = float(input("Enter ending odometer reading => "))
n = 1.50
c = b - a
x = "{:.2f}".format(c)
d = c * n
y = "{:.2f}".format(d)
print(f"You traveled a distance of {x} miles. At {n} per mile, your fare is {y}.")