#ROSETTE GONE WILD

#import turtle
#t = turtle.Pen()
#number_of_circles = int(turtle.numinput("Number of cirlces", "How many cirlces in your rosette?", 6))
#for x in range(number_of_circles):
#    t.circle(100)
#    t.left(360/number_of_circles)
#    t.circle(100)
#    t.left(360/number_of_circles)
#    t.circle(100)
#    t.left(360/number_of_circles)
#    t.circle(100)

#___________________________________
#SAY OUR NAMES

#name = input("What is your name? ")

#while name != "":

#    for x in range(100):

#        print(name, end = " ")
#    print()

#    name = input("Type another name, or just hit [ENTER] to quit: ")
#print("Thanks for playing!")
                 
#____________________________________
#SPIRAL FAMILY

#import turtle
#t = turtle.Pen()
#turtle.bgcolor("black")
#colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "brown", "gray", "pink" ]
#family = []
#name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")
#while name != "":
#    family.append(name)
#    name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")#

#    for x in range(100):
#        t.pencolor(colors[x%len(family)])
#        t.penup()
#        t.forward(x*4)
#        t.pendown()
#        t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
#        t.left(360/len(family) + 2)
#_____________________________________
#SPIRAL GOES VIRAL

#for x in range(10):

#    for y in range(10):
#
#        import turtle
#        t = turtle.Pen()
#        t.penup()
#        turtle.bgcolor("black")
#        sides = int(turtle.numinput("Number of sides", "How many sides in your spiral of spirals (2-6)?", 4,2,6))
#        colors = ["red", "yellow", "blue", "green", "purple", "orange"]
#        for m in range(100):
#            t.forward(m*4)
#            position = t.position()
#            heading = t.heading()

#            for n in range(int(m/2)):
#                t.pendown()
#                t.pencolor(colors[n%sides])
#                t.forward(2*n)
#                t.right(360/sides - 2)
#                t.penup
#            t.setx(position[0])
#            t.sety(position[1])
#            t.setheading(heading)
#            t.left(360/sides + 2)
