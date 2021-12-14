from random import randint
computer_score=0
player_score=0
choice_count=0

while True:
    print("\n 1. rock\n 2. paper\n 3. scissors\n ")
    choice= int(input("Make your choice: "))
    choice_count+=1
    
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        nameof_choice = 'rock'
    elif choice == 2:
        nameof_choice = 'paper'
    else:
        nameof_choice = 'scissors'
    print("user choice is: " ,nameof_choice)

    comp_choice = randint(1, 3)
    
    
    if comp_choice == 1:
        nameof_comp_choice = 'rock'
    elif comp_choice == 2:
        nameof_comp_choice = 'paper'
    elif comp_choice == 3:
        nameof_comp_choice = 'scissors'
        
    print("Computer choice is: " + nameof_comp_choice)
      
    print(nameof_choice + " : " + nameof_comp_choice)
    
    if choice == comp_choice:
        print("\nDraw!!!")
    
    elif (choice == 1 and comp_choice == 2) or (choice == 3 and comp_choice == 1) or (choice == 2 and comp_choice == 3):
        computer_score+=1
        print("1 point to computer\n", end = "")
    else:
        player_score+=1
        print("1 point to player\n", end = "")        
                  
        
    if choice_count == 3:
        if computer_score > player_score:
            print("\nComputer wins ")
        elif computer_score < player_score:
            print("\nPlayer wins")
        else:
            print("\nDraw")
              
        print("Do you want to play again? (press 'N/n' to quit)")
        answer = input()
        if answer == 'n' or answer == 'N':
            break
        choice_count = 0
        computer_score = 0
        player_score = 0