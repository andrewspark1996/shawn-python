#GUESSING GAME

#import random
#the_number = random.randint(1, 10)
#guess = int(input('Guess a number between 1 and 10: '))
#while guess != the_number:
#    if guess > the_number:
#        print(guess, 'was too high. Try again.')
#    if guess < the_number:
#        print(guess, 'was too low. Try gain.')
#    guess = int(input('Guess again: '))
#print(guess, 'was the number! You win a pickle factory!')


#RANDOM SPIRALS

#import random
#import turtle
#t = turtle.Pen()
#turtle.bgcolor('black')
#colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray']
#for n in range(50):
#    t.pencolor(random.choice(colors))
#    size = random.randint(10, 40)
#    x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
#    
#    y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)
#

 #   t.penup()
 #   t.setpos(x,y)
 #   t.pendown()
 #   for m in range(size):
 #       t.forward(m*2)
 #       t.left(91)


#ROCK PAPER SCISSORS

import random
choices = ['rock' 'paper', 'scissors']
print('Rock crushes scissors. Scissors cut paper. Paper covers rock.')
player = input('Do you want to be rock, paper, or scissors (or quit)? ')
while player != 'quit':
    player = player.lower()
    computer = random.choice(choices)
    print('You chose ' +player+ ', and te computer chose ' +computer+ '.')
    if player == computer:
        print("It's a tie!")
    elif player == 'rock':
        if computer == 'scissors':
            print('You win a pickle peeler')
        else:
            print('Computer wins!')
    elif player == 'paper':
        if computer == 'rock':
            print("You win a pickle shaver!")
        else:
            print('Computer wins!')





 
