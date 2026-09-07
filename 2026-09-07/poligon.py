# programa que llegeix la mida i el nombre de costats d'un polígon i dibuixa el polígon regular

import turtle

mida = int(input())
costats = int(input())

n = 0
while n < costats:
    turtle.forward(mida)
    turtle.right(360 / costats)
    n = n + 1

turtle.done()
