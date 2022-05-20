h = float(input("input hour   : "))
m = float(input("input mintue : "))
M = m / 60
t = h + M
T = ((4 * (t * t)) / (t + 2)) - 20
x = "{:.2f}".format(T)
print(f"temp : {x}")