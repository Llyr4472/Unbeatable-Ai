import os 

print('Llŷr :)')
match = True
turns =0
while match == True:
    print("""        

                                        TIC TAC TOE   

                                        ¦      ¦
                                     A1 ¦  B1  ¦  C1
                                  —————— —————— ——————
                                        ¦      ¦
                                     A2 ¦  B2  ¦  C2
                                  —————— —————— ——————
                                        ¦      ¦  
                                     A3 ¦  B3  ¦  C3
    """)
    p1 = True
    p1win = p2win = False
    move =""
    A1,A2,A3,B1,B2,B3,C1,C2,C3=" "," "," "," "," "," "," "," "," "
    Player1 = str.capitalize(input("Enter Player1's name:\n"))
    Player2 = str.capitalize(input("Enter Player2's name:\n"))
    if Player1 == '':
        Player1 = 'Player1'
    elif Player2 == '':
        Player2 = 'Player2'
    os.system("cls")
    print('Llŷr :)')
    while not p1win or p2win:
        print(f"""        

                                        TIC TAC TOE   

                                    A     B      C
                                        ¦      ¦
                                1     {A1} ¦  {B1}   ¦  {C1}
                                  —————— —————— ——————
                                        ¦      ¦
                                2     {A2} ¦  {B2}   ¦  {C2}
                                  —————— —————— ——————
                                        ¦      ¦  
                                3     {A3} ¦  {B3}   ¦  {C3}
        """)
        loop = True
        while loop:
            loop= False
            if p1:
                turn = 'X'
                print(f"{Player1}'s turn")
            elif not p1:
                turn = 'O'
                print(f"{Player2}'s turn")
            move = input()
            if str.capitalize(move)== "A1" and A1 == ' ':
                A1 = turn
            elif str.capitalize(move)== "A2" and A2 == ' ':
                A2 = turn
            elif str.capitalize(move)== "A3" and A3 == ' ':
                A3 = turn
            elif str.capitalize(move)== "B1" and B1 == ' ':
                B1 = turn
            elif str.capitalize(move)== "B2" and B2 == ' ':
                B2 = turn
            elif str.capitalize(move)== "B3" and B3 == ' ':
                B3 = turn
            elif str.capitalize(move)== "C1" and C1 == ' ':
                C1 = turn
            elif str.capitalize(move)== "C2" and  C2 == ' ':
                C2 = turn
            elif str.capitalize(move)== "C3" and C3 == ' ':
                C3 = turn
            else:
                print("\n Invalid move")
                loop = True
            if loop != True:
                os.system('cls')
                print('Llŷr :)')
                p1 = not p1
            turns += 1
        p1win = A1==A2==A3=='X' or A1==B1==C1=='X' or A2==B2==C2=='X' or A3==B3==C3=='X' or B1==B2==B3=='X' or C1==C2==C3=='X' or A1==B2==C3=='X' or C1==B2==A3=='X'
        p2win = A1==A2==A3=='O' or A1==B1==C1=='O' or A2==B2==C2=='O' or A3==B3==C3=='O' or B1==B2==B3=='O' or C1==C2==C3=='O' or A1==B2==C3=='O' or C1==B2==A3=='O'
        if turns == 9:
            break
    if p1win:
        print("\n Congratulations!!! ", Player1, 'won')
    elif p2win:
        print('\n Congratulations!!!', Player2, 'won.')
    elif turns == 9:
        print('Its a tie.')
    if input("\n Rematch? (y/n)") == 'n':
        match = False
    os.system('cls')

