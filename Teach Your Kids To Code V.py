#IF SPIRAL

#answer = input("Do you want to see a spiral? y/n:")
#if answer == 'y':
#    print("Working...")
#    import turtle
#    t = turtle.Pen()
 #   t.width(2)
 #   for x in range(100):
#        t.forward(x*2)
#        t.left(89)
#print("Okay, we're done!")

#OLD ENOUGH OR ELSE

#driving_age = eval(input("What is the legal driving age where you live? "))
#your_age = eval(input("How old are you? "))
#if your_age <= driving_age:
#    print("You're old enough to dirve!")
#if your_age > driving_age:
#    print("Sorry, you can drive in", driving_age - your_age, "years.")

#POLYGON OR ROSETTE

#import turtle
#t = turtle.Pen()
#number = int(turtle.numinput('Number of sides or circles', 'How many sides or circles in your shape?', 6))
#shape = turtle.textinput('Which shape do you want?', 'Enter "p" for polygon or "r" for rosette:')
#for x in range(number):
#    if shape == 'r':
 #       t.circle(100)
#    else:
    #    t.forward (150)
#    t.left(360/number)

#ROSETTES AND POLYGONS

#import turtle
#t = turtle.Pen()

#sides = int(turtle.numinput('Number of sides', 'How many sides in your spiral?', 4))

#for m in range(5,75):
#    t.left(360/sides + 5)
#    t.width(m//25+1)
#    t.penup()
#    t.forward(m*4)
#    t.pendown()

#    if (m % 2 == 0):
#        for n in range(sides):
#            t.circle(m/3)
#            t.right(360/sides)

 #   else:
  #      for n in range(sides):
   #         t.forward(m)
    #        t.right(360/sides)


#WHAT'S MY GRADE

#grade = eval(input("Enter your number grade(0-100): "))
#if grade >= 90:
#    print("You got an A! :) ")
#elif grade >= 80:
#    print("You got a B!")
#elif grade >= 70:
#    print("You got a C.")
#elif grade >= 60:
#    print("You got a D...")
#else:
#    print("You got a F!!!>:(")


#WHAT TO WEAR

#rainy = input("How's the weather? Is it raining? (y/n)").lower()
#cold = input("Is it cold outside? (y/n)").lower()
#if (rainy == 'y' and cold == 'y'):
#    print("You'd better wear a raincoat.")
#elif (rainy == 'y' and cold != 'y'):
#    print("Carry an umbrella with you.")
#elif (rainy != 'y' and cold == 'y'):
#    print("Put on a jacket, it's cold out!")
#elif (rainy != 'y' and cold != 'y'):
#    print("Wear whatever you want, it's beautiful outside!")


#ENCODER DECODER

#message = input('Enter a message to encode or decode: ')
#message = message.upper()
#output = ""
#for letter in message:
#    if letter.isupper():
#        value = ord(letter) + 13
#        letter = chr(value)
#        if not letter.isupper():
#            value -= 26
#            letter = chr(value)
#    output += letter
#print('Output message: ', output)
            
