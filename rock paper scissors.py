print("Rock Paper and scissors game")
print("r=rock ; p=paper ; s=scissors")
choice1=input("Player 1 enter your choice: ")
choice2=input("Player 2 enter your choice: ")
if(choice1=='r'):
    if(choice2=='s'):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif(choice1=='p'):
    if(choice2=='r'):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif(choice1=='s'):
    if(choice2=='p'):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    print("Invalid chioice!!!Choose only between r,s,p")
print("Thanks for Playing!!!")


