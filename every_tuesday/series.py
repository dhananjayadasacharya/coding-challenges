n = int(input("Enter n: "))
seq=[5]


a,b=1,1

for _ in range(1,n):
    seq.append(seq[-1]+a)
    a,b = b,a+b

print(seq)