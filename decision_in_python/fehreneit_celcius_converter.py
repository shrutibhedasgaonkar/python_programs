F = float(input("Enter temperature = "))
C = 5/9*(F-32)

if C < 0:
    print(f"{C:.2f}", "degrees is Freezing Temperature")
elif 0 <= C <= 15:
    print(f"{C:.2f}", "degrees is Cold Temperature")
elif 16 <= C <= 30:
    print(f"{C:.2f}", "degrees is Warm Temperature")

else:
    print(f"{C:.2f}", "degrees is Hot Temperature")




