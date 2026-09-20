import turtle

angle = 10
costats = 5
for j in range(360 // angle):
    for i in range(costats):
        turtle.forward(100)
        turtle.right(360 / costats)
    turtle.right(angle)

turtle.done()
