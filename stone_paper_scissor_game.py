""" In this Game
    We will Design a game - stone paper scissor
    where user will play against the bot 
    bot will select a choice from the elements [stone , paper ,scissor]
    where as , user will also choose an input ,
    and the winner will gets some points"""

elements=['stone','paper','scissor']

import random
bot_choice=random.choice(elements)

user_choice=input("Choose from ['stone','paper','scissor'] :")

print("bot choose :",bot_choice)

if user_choice==bot_choice:
    print("Its a tied...")
else:
    if user_choice=='stone' and bot_choice=='paper':
        print('bot wins')
    elif user_choice=='paper' and bot_choice=='stone':
        print('user wins')
    elif user_choice=='stone' and bot_choice=='scissor':
            print('user wins')
    elif user_choice=='scissor' and bot_choice=='stone':
            print('bot wins')
    elif user_choice=='paper' and bot_choice=='scissor':
            print('bot wins')  
    elif user_choice=='scissor' and bot_choice=='paper':
            print('user wins')
    else:
        print("choose right element from ['stone','paper','scissor'] ")