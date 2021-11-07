from to_class import Game
from bot import BotGame
from bot_hard import BotGame_hard
class Game_logic():
    def __init__(self):
        pass
    
    def play(self):
        print('Welcome to the tic tac toe game')
        
        print("Player 1")
        print("Enter the name : ")
        player1=input('> ')
        print("\n")
    
        print("Player 2")
        print('type y to play with bot and n to play with other player ?')
        choice=input('> ')
        if choice == 'y':
            player2 ='bot'
            game=BotGame_hard()
            print("\n")
        elif choice == 'n':
            print("Enter the name : ")
            player2 =input('> ')
            print("\n")
            game=Game()
        
        # Stores the player who chooses X and O
        cur_player = player1
    
        # Stores the choice of players
        player_choice = {'X' : "", 'O' : ""}
    
        # Stores the options
        options = ['X', 'O']
    
        # Stores the scoreboard
        score_board = {player1: 0, player2: 0}
        game.print_scoreboard(score_board)
    
        # Game Loop for a series of Tic Tac Toe
        # The loop runs until the players quit 
        while True:
    
            # Player choice Menu
            print("Turn to choose for ", cur_player)
            print("Enter 1 for X")
            print("Enter 2 for O")
            print("Enter 3 to Quit")
    
            # Try exception for CHOICE input
            try:
                choice = int(input("> "))   
            except ValueError:
                print("Wrong Input!!! Try Again\n")
                continue
    
            # Conditions for player choice  
            if choice == 1:
                player_choice['X'] = cur_player
                if cur_player == player1:
                    player_choice['O'] = player2
                else:
                    player_choice['O'] = player1
    
            elif choice == 2:
                player_choice['O'] = cur_player
                if cur_player == player1:
                    player_choice['X'] = player2
                else:
                    player_choice['X'] = player1
            
            elif choice == 3:
                print("Final Scores")
                game.print_scoreboard(score_board)
                break  
    
            else:
                print("Wrong Choice!!!! Try Again\n")
    
            # Stores the winner in a single game of Tic Tac Toe
            winner = game.single_game(options[choice-1],player_choice)
            
            # Edits the scoreboard according to the winner
            if winner != 'D' :
                player_won = player_choice[winner]
                score_board[player_won] = score_board[player_won] + 1
    
            game.print_scoreboard(score_board)
            # Switch player who chooses X or O
            if cur_player == player1:
                cur_player = player2
            else:
                cur_player = player1 



if __name__=='__main__':
    game=Game_logic()
    game.play()



        