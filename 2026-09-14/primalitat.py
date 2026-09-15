# programa que diu si un natural és primer o no

import yogi

n = yogi.read(int)

if n < 2:
    print("no")
else:
    c = 0
    i = 2
    while i * i <= n and c == 0:
        if n % i == 0:
            c = c + 1
        i = i + 1
    if c == 1:
        print("no")
    else:
        print("si")
