P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))

SI = (P*R*T)/100
Amount = P+SI

print("Simple Interest =", SI)
print("Total Amount =", Amount)
