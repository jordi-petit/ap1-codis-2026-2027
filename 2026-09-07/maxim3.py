# programa que llegeix tres números i escriu el més gran

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    m = a
elif b >= a and b >= c:
    m = b
else:
    m = c

print(m)
