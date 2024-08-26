def print_board(board):# function to draw bord
    for i in range(3):#runs line by line to print bord
        print(board[3*i] + ' | ' + board[3*i+1] + ' | ' + board[3*i+2]) #it will place first three elemet of array bord in first tree lines and so on
        if i<2:
            print('---------')# check condition and print dash line to seprate line one and and line two 
def check_winner(board,player):#function for checking the winner
    win_conditions=[(0,1,2),(3,4,5),(6,7,8), 
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]#possible winning conditions saved as each tuple
    for condition in win_conditions:#loops each tuple from condition list
        if board[condition[0]]==board[condition[1]]==board[condition[2]]==player:#checks bored array index with each condition value from tuple are frome same player
            return True
    return False
def check_draw(board):#function for checking the draw
    return ' 'not in board#returns true if no empty space and false if any
def minimax(board,depth,is_maximizing,alpha=-float('inf'),beta=float('inf')):#fuction to implement ai algorithm
    if check_winner(board,'O'):#call winner functuion for winner of O
        return 1
    elif check_winner(board,'X'):#call winner functuion for winner of X
        return -1
    elif check_draw(board):#call draw function
        return 0
    if is_maximizing:#if minimax is true run if part
        best_score=-float('inf')#lowest lossing score
        for i in range(9):#loop for playing game for next 9 times
            if board[i]==' ':#check for empty space
                board[i]='O'#print O in empty space
                score=minimax(board,depth + 1,False,alpha,beta)#recursive call of same funtion but to play with next oppenent of next lever or next move and conti ue from there
                board[i]=' '#re-do the printed O
                best_score=max(score,best_score)#check mximum score between gaind result and defult result
                alpha=max(alpha,score)#maximum of score between maximum player and minimum player i.e of diffrent branchers to parent branch
                if beta<=alpha:#condition for braking the loop
                    break
        return best_score#if broke loop return best score
    else:
        best_score=float('inf')#highest lossing score
        for i in range(9):#loop for playing game for next 9 time
            if board[i]==' ':#check for empty space
                board[i]='X'#print X in empty space
                score=minimax(board,depth + 1,True,alpha,beta)#recursive call of same funtion but to play with next oppenentof next lever or next move and conti ue from there
                board[i]=' '#re-do the printed X
                best_score=min(score,best_score)#check mximum score between gaind result and defult result
                beta=min(beta,score)#minimum of score between maximum player and minimum player  i.e of diffrent branchers to parent branch
                if beta<=alpha:#condition for braking the loop
                    break
        return best_score #broke loop return best score
def ai_move(board):#function to inciate ai move with minimax algorithm
    best_score=-float('inf')#lowest lossing score
    best_move=0#to place the O on the best winning position
    for i in range(9):#loop for playing game for next 9 time
        if board[i]==' ':#check for empty space
            board[i]='O'#print O in empty space
            score=minimax(board,0,False)#recursive call of minimax funtion to virtually play with next oppenent of next lever or next move and contiue from there and store valee
            board[i]=' '#re-do the printed O
            if score>best_score:#contion to check ai got winning score of 1 
                best_score=score#change values
                best_move=i#place O in winning position related to score
    board[best_move]='O'#print O on the position
def human_move(board,move):# function to input human move
    if board[move]==' ':#check for empty space
        board[move]='X'#print X in empty space
    else:
        print("Invalid move! Try again.")
def play_game():# first running function
    board=[' ' for _ in range(9)]# create 9 empty space to print the board
    while True:# to run loop with know condition
        print_board(board)#print board after each move
        # Human turn
        move=int(input("Enter your move (1-9): "))-1#input string with -1
        human_move(board,move)#initiating human move function
        if check_winner(board,'X'):#check winner for x and print board
            print_board(board)
            print("You win!")#declere winn
            break
        if check_draw(board):#check draw condition 
            print_board(board)
            print("It's a draw!")#declere draw
            break
        # AI turn
        ai_move(board)#initiating ai move function
        if check_winner(board,'O'):#check winner for O and print board
            print_board(board)
            print("AI wins!")#declere winn
            break
        if check_draw(board):#check draw condition 
            print_board(board)
            print("It's a draw!")#declere draw
            break
play_game()#call function to fun first
