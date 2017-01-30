import turtle

window = turtle.Screen()
window.bgcolor("yellow")
    
def draw_init():
    saha = turtle.Turtle()
    saha.left(45)
    saha.forward(120)
    saha.right(90)
    saha.forward(120)
    saha.backward(50)
    saha.right(135)
    saha.forward(100)

    saha.penup()
    saha.goto(230,90)
    saha.pendown()
    saha.forward(50)
    saha.left(90)
    saha.forward(50)
    saha.left(90)
    saha.forward(50)
    saha.right(90)
    saha.forward(50)
    saha.right(90)
    saha.forward(50)
    
turt = turtle.Turtle()
turt.speed=8
def triangles(marker, order, size):
    for i in range(3):
        marker.forward(size)
        marker.right(120)
        if order>0:
            triangles(marker, order-1, size/2)

triangles (turt, 4, 200)
