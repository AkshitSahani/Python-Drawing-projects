import turtle

def draw_square(some_turtle):
    i=0
    while i<4:
        some_turtle.forward(100)
        some_turtle.right(90)
        i+=1

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

#def draw_circle():
#    window = turtle.Screen()
#    window.bgcolor("yellow")
#
#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("red")
#    angie.circle(100)

#def draw_triangle():
#    window = turtle.Screen()
#    window.bgcolor("yellow")

#    tom = turtle.Turtle()
#    tom.shape("turtle")
#    tom.color("pink")

#    i=0
#    while i<3:
#        tom.forward(100)
#        tom.right(120)
#        i+=1


draw_art()

#draw_circle()

#draw_triangle()
