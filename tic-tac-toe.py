#Tic-Tac-Toe
def box():
    print()
    print("----------------------------------")
    print(f" 7 | 8 | 9        {ls[6]} | {ls[7]} | {ls[8]} ")
    print( "---+---+---      ---+---+---")
    print(f" 4 | 5 | 6        {ls[3]} | {ls[4]} | {ls[5]} ")
    print( "---+---+---      ---+---+---")
    print(f" 1 | 2 | 3        {ls[0]} | {ls[1]} | {ls[2]} ")
    print("----------------------------------")
    # print(f"Moves made by max: {l1[0]}")
    # print(f"Moves made by user: {l2[0]}")
    # print(f"Moves made by Computer: {l3[0]}")
    print()

"""
Indexing

     6 | 7 | 8 
    ---+---+---
     3 | 4 | 5 
    ---+---+---
     0 | 1 | 2 
     
"""


def winner(player):

    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for i in win:
        if ls[i[0]] == ls[i[1]] == ls[i[2]] == player:
            return True
    return False

def is_draw():
    if ' ' in ls:
        return False
    return True

def brain(is_max):
    
    if winner('X'):
        return -1
    
    if winner('O'):
        return 1
    
    if is_draw():
        return 0
    

    if is_max:              #Computer's turn

        best = -10

        for i in range(9):
            if ls[i] == ' ':
                ls[i] = 'O'
                # l1[0] += 1 
                score = brain(False)
                ls[i] = ' '
                if score > best:
                    best = score

        return best
    
    else:  # User's turn
        best = 10

        for i in range(9):
            if ls[i] == ' ':
                ls[i] = 'X'
                # l2[0] += 1 
                score = brain(True)
                ls[i] = ' '
                if score < best:
                    best = score

        return best

def computer():

    best_ = -10
    move = None

    for i in range(9):
        if ls[i] == ' ':
            ls[i] = 'O'
            # l3[0] += 1 
            score = brain(False)
            ls[i] = ' '

            if score > best_:
                best_ = score
                move = i
    
    ls[move] = 'O'

#l1, l2, l3 = [0], [0], [0]
ls = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while True:
    while True:

        box()

        while True:
            try:
                p = int(input("Enter your position (1-9): "))

                if p > 9 or p < 1:
                    raise ValueError("Please enter a number between 1 and 9.")

                if ls[p-1] == ' ':
                    ls[p-1] = 'X'
                    break

                else:
                    raise Exception("Position already taken.")

            except ValueError:
                print("Enter a number only.")  
                
            except Exception as e:
                print(f"Error: {e}.\nPlease try again.")      
            
        
        if winner('X'):
            box()
            print("You Win!")
            break

        if is_draw():
            box()
            print("Draw!")
            break
        
        computer()

        if winner('O'):
            box()
            print("Computer Win!")
            break

        if is_draw():
            box()
            print("Draw!")
            break
    
    b = input("Do you want to continue (y/n): ").lower()
    if b == 'y':
        ls = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # l1,l2,l3 = [0],[0],[0]
        continue
    else:
        print("Good bye!")
        break