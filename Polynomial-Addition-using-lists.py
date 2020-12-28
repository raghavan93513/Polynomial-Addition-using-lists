n1 = int(input())
a = []
for i in range(n1+1):
    a.append(int(input()))
n2 = int(input())
b = []
for i in range(n2+1):
    b.append(int(input()))

if len(a) > len(b):
    big = a
    smol = b
else:
    big = b
    smol = a

for i in range(1,len(smol)+1):
    big[-i] = big[-i] + smol[-i]
print(big)