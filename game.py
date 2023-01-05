import random
print('''
_________________________________________________________________
|                                                               |
|    Welcome to the Number Guessing Game!                       |
|                                                               |
|    Instructions:                                              |
|        1. Total 3 lifes given                                 |
|        2. Select the number range form 0                      |
|        3. guess the number                                    |
|        4. if correct ? Hurray, You've won! else You lose!     |
|_______________________________________________________________|
''')

name = input("Enter Your Name -> ")
limit = int(input("Enter your range -> "))

print(f'\n\nWelcome {name} to the Number Guessing Game!')

while 1:
    num = random.randint(0,limit)
    lifes = 3
    while lifes:
        print()
        choice = int(input("\n Enter your choice -> "))
        flag = True
        if choice == num:
            print("Hurray! You've won the Game")
		print('''
		________________________________________________
		|								|
		|	You							|
		|	  Won							|
		|	   The						|
		|	    Game						|				
		|_______________________________________________|
            flag = False
            break
        print("Wrong Choice, choose again!")
        lifes -= 1
    if flag:
        print("\n Better luck next time!")
    
    repeat = input("\n\n Do you want to play again ? (yes/no) ").lower()
    if repeat=='yes':
        pass
    else:
        print(f"\n\n Thank you for playing {name}!")
        break
