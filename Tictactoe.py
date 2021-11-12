board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def draw_board():
    for i in range(3):
        print()
        for j in range(3):
            print(board[i][j], end='')
            if j<2:
                print('|', end='')
    print()


def take_input():
    pos=input("Enter a number :")
    pos=int(pos)-1 # because in array value start from zero
    if pos <= 9:
        return pos
    else:
        pos = input("Enter a number")
        pos = int(pos) - 1

def place_player(pos, player):
    row = pos//3 
    column = pos % 3
    if board[row][column] == '-': 
        board[row][column]= player
        return 1
    else:
        print("Sorry Wrong value")
        return 0

def check_tie():
    for i in range(3):
        for j in range(3):
            if board[i][j]=='-':

                return
            else:
                continue
    print("The Game is tied")
    game_on = False

def check_column(j):
    x=0
    o=0
    for i in range(3):
        if board[i][j]=='X':
            x=x+1
        if board[i][j] == 'O':
            o = o + 1

    if x ==3:
        print("X won")
        return game_on == False

    if o == 3:
        print("O won")
        return game_on == False

    else:
        return game_on == True

def check_row(i):
    x=0
    o=0
    for j in range(3):
        if board[i][j]=='X':
            x=x+1
        if board[i][j] == 'O':
            o = o + 1
    if x ==3:
        print("X won")
        return game_on == False

    if o == 3:
        print("O won")
        return game_on == False

    else:
        return game_on == True

def check(a, b, c):
    var = [a, b, c]
    x=0
    o=0
    for i in var:
        if i=='X':
             x += 1
        elif i == 'O':
            o += 1
    if x ==3:
        print("X won")
        return game_on == False

    if o == 3:
        print("O won")
        return game_on == False

    else:
        return game_on == True
    
    
def main():
    global game_on #by global we can use game_on in any function
    count=0
    game_on=True
    while game_on:
        if count % 2 == 0:
            player = 'X'
        else:
            player = 'O'
       
        pos=take_input() #taking player
        count = count + place_player(pos, player)
        for j in range(3):
            game_on = check_column(j)
            game_on = check_row(j)
        check_tie()
        check(board[0][0], board[1][1], board[2][2])
        check(board[0][2], board[1][1], board[2][0])
        draw_board()
       
main()

#draw_board()