# write your code here
player1 = 'X'
player2 = 'O'

cell_values = "         "
cell_values = list(cell_values)

print("-" * 9)
print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
print("-" * 9)

turn = player1
X_count = [x for x in cell_values if x == 'X']
O_count = [o for o in cell_values if o == 'O']
win_counter = 0
x_wins = 0
o_wins = 0
s = True
while s:
    print("Enter the coordinates: ")
    co_list = input().split()
    co1 = co_list[0]
    co2 = co_list[1]
    if not co1.isdigit() and not co2.isdigit():
        print("You should enter numbers!")
    co1 = int(co1)
    co2 = int(co2)
    if co1 < 1 and co1 > 3 and co2 < 1 and co2 > 3:
        print("Coordinates should be from 1 to 3!")
    elif co1 == 1:
        if co2 == 1:
            if cell_values[6] == ' ':
                cell_values[6] = cell_values[6].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
        elif co2 == 2:
            if cell_values[3] == ' ':
                cell_values[3] = cell_values[3].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
        elif co2 == 3:
            if cell_values[0] == ' ':
                cell_values[0] = cell_values[0].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
    elif co1 == 2:
        if co2 == 1:
            if cell_values[7] == ' ':
                cell_values[7] = cell_values[7].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
        elif co2 == 2:
            if cell_values[4] == ' ':
                cell_values[4] = cell_values[4].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
        elif co2 == 3:
            if cell_values[1] == ' ':
                cell_values[1] = cell_values[1].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
    elif co1 == 3:
        if co2 == 1:
            if cell_values[8] == ' ':
                cell_values[8] = cell_values[8].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
        elif co2 == 2:
            if cell_values[5] == ' ':
                cell_values[5] = cell_values[5].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
        elif co2 == 3:
            if cell_values[2] == ' ':
                cell_values[2] = cell_values[2].replace(' ', turn)
                print("-" * 9)
                print("| " + cell_values[0] + " " + cell_values[1] + " " + cell_values[2] + " |")
                print("| " + cell_values[3] + " " + cell_values[4] + " " + cell_values[5] + " |")
                print("| " + cell_values[6] + " " + cell_values[7] + " " + cell_values[8] + " |")
                print("-" * 9)
                X_count = [x for x in cell_values if x == 'X']
                O_count = [o for o in cell_values if o == 'O']
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                print("This cell is occupied! Choose another one!")
    if cell_values[0] == 'X' and cell_values[0] == cell_values[1] and cell_values[1] == cell_values[2]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[0] == 'O' and cell_values[0] == cell_values[1] and cell_values[1] == cell_values[2]:
        o_wins += 1
        win_counter += 1
        s = False
    elif cell_values[0] == 'X' and cell_values[0] == cell_values[3] and cell_values[3] == cell_values[6]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[0] == 'O' and cell_values[0] == cell_values[3] and cell_values[3] == cell_values[6]:
        o_wins += 1
        win_counter += 1
        s = False
    elif cell_values[1] == 'X' and cell_values[1] == cell_values[4] and cell_values[4] == cell_values[7]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[1] == 'O' and cell_values[1] == cell_values[4] and cell_values[4] == cell_values[7]:
        o_wins += 1
        win_counter += 1
        s = False
    elif cell_values[2] == 'X' and cell_values[2] == cell_values[5] and cell_values[5] == cell_values[8]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[2] == 'O' and cell_values[2] == cell_values[5] and cell_values[5] == cell_values[8]:
        o_wins += 1
        win_counter += 1
        s = False
    elif cell_values[3] == 'X' and cell_values[3] == cell_values[4] and cell_values[4] == cell_values[5]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[3] == 'O' and cell_values[3] == cell_values[4] and cell_values[4] == cell_values[5]:
        o_wins += 1
        win_counter += 1
        s = False
    elif cell_values[6] == 'X' and cell_values[6] == cell_values[7] and cell_values[7] == cell_values[8]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[6] == 'O' and cell_values[6] == cell_values[7] and cell_values[7] == cell_values[8]:
        o_wins += 1
        win_counter += 1
        s = False
    elif cell_values[0] == 'X' and cell_values[0] == cell_values[4] and cell_values[4] == cell_values[8]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[0] == 'O' and cell_values[0] == cell_values[4] and cell_values[4] == cell_values[8]:
        o_wins += 1
        win_counter += 1
        s = False
    elif cell_values[2] == 'X' and cell_values[2] == cell_values[4] and cell_values[4] == cell_values[6]:
        x_wins += 1
        win_counter += 1
        s = False
    elif cell_values[2] == 'O' and cell_values[2] == cell_values[4] and cell_values[4] == cell_values[6]:
        o_wins += 1
        win_counter += 1
        s = False
    elif ' ' not in cell_values:
        s = False
if x_wins > 0:
    print("X wins")
elif o_wins > 0:
    print("O wins")
elif x_wins == 0 and o_wins == 0:
    print("Draw")
