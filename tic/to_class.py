from abc import abstractclassmethod


class Game:
    def __init__(self) -> None:
        pass
    def print_tic_tac_toe(self,values):
        print("\n")
        print("    |     |")
        print(" {}  |  {}  |  {}".format(values[0], values[1], values[2]))
        print('____|_____|_____')
    
        print("    |     |")
        print(" {}  |  {}  |  {}".format(values[3], values[4], values[5]))
        print('____|_____|_____')
    
        print("    |     |")
    
        print(" {}  |  {}  |  {}".format(values[6], values[7], values[8]))
        print("    |     |")
        print("\n")
    
    
    # Function to print the score-board
    @abstractclassmethod
    def print_scoreboard(cls,score_board):
        print("--------------------------------")
        print("              SCOREBOARD        ")
        print("--------------------------------")
    
        players = list(score_board.keys())
        print(f"    {players[0]}  ====>  {str(score_board[players[0]])}")
        print(f"    {players[1]}  ====>  {str(score_board[players[1]])}")
    
        print("--------------------------------\n")
        return"""
        --------------------------------
                      SCOREBOARD        
        --------------------------------
            player1  ====>  0
            player2  ====>  0
        --------------------------------
        """
    # Function to check if any player has won
    def check_win(self,player_pos, cur_player):
    
        # All possible winning combinations
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
        # Loop to check if any winning combination is satisfied
        for x in soln:
            if all(y in player_pos[cur_player] for y in x):
    
                # Return True if any winning combination satisfies
                return True
        # Return False if no combination is satisfied       
        return False       
    
    # Function to check if the game is drawn
    def check_draw(self,player_pos):
        if len(player_pos['X']) + len(player_pos['O']) == 9:
            return True
        return False       
    
    # Function for a single game of Tic Tac Toe
    def single_game(self,cur_player):
    
        # Represents the Tic Tac Toe
        values = [' ' for x in range(9)]
        
        # Stores the positions occupied by X and O
        player_pos = {'X':[], 'O':[]}
        
        # Game Loop for a single game of Tic Tac Toe
        while True:
            self.print_tic_tac_toe(values)
            
            # Try exception block for MOVE input
            try:
                print("Player ", cur_player, " turn. Which box? : ")
                move = int(input("> ")) 
            except ValueError:
                print("Wrong Input!!! Try Again")
                continue
    
            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print("Wrong Input!!! Try Again")
                continue
    
            # Check if the box is not occupied already
            if values[move-1] != ' ':
                print("Place already filled. Try again!!")
                continue
    
            # Update game information
    
            # Updating grid status 
            values[move-1] = cur_player
    
            # Updating player positions
            player_pos[cur_player].append(move)
    
            # Function call for checking win
            if self.check_win(player_pos, cur_player):
                self.print_tic_tac_toe(values)
                print("Player ", cur_player, " has won the game!!")     
                print("\n")
                return cur_player
    
            # Function call for checking draw game
            if self.check_draw(player_pos):
                self.print_tic_tac_toe(values)
                print("Game Drawn")
                print("\n")
                return 'D'
    
            # Switch player moves
            if cur_player == 'X':
                cur_player = 'O'
            else:
                cur_player = 'X'
# if __name__ == "__main__":
#     def play():
                       