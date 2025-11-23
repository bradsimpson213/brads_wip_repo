import os
from time import sleep
from logo import logo, instructions
from display import print_display


class TicTacToe:
    """Class that creates instances of the Tic Tac Toe Game"""
    def __init__(self):
        """Constructor to set up a game"""
        self.board = [' ', ' ', ' ', 
                      ' ', ' ', ' ', 
                      ' ', ' ', ' ',
                      ]
        self.player1 = None
        self.player2 = None
        self.player_turn = 1
        self.play_game()


    def set_player_type(self, player_num):
        """Method to set up the players, either human or computer controlled"""
        while True:
            user_input = input(f"Is Player {player_num} a Human or a Computer? (enter H or C) ").upper()
            if user_input == "H":
                return "Human"
            elif user_input == "C":
                return "Computer"
            else:
                os.system("cls")
                print(f'Incorrect input of "{user_input}", try again!')


    def human_move(self):
        """Method to handle human input and save move to the board"""
        print(instructions, end="")
        while True:
            try:
                play_loc = (int(input(f"Player{self.player_turn} '{'X' if self.player_turn == 1 else 'O'}' enter a number 1-9 to make your move: ")) - 1)

            except TypeError:
                print(f"You entered {play_loc}, please enter a number 1-9")
                continue

            except ValueError:
                print(f"You entered an incorrect value, please enter a number 1-9")
                continue

            else:
                if play_loc not in range(0, 10):  # end value not inclusive in range built-in
                    print(f"You entered {play_loc}, please enter a number 1-9")
                    continue

                if self.board[play_loc] != ' ':
                    print(f"{self.board[play_loc]} has already played in that space, try again!")
                    continue

                else:
                    self.board[play_loc] = "X" if self.player_turn == 1 else "O"
                    return
        


    def computer_move(self):
        """Method to control a computer player, using a minimax algorithm"""
        
        best_score = float("-inf")
        best_move = None
        for index, move in enumerate(self.board):
            if move == ' ':
                self.board[index] = "X" if self.player_turn == 1 else "O"
                score = self.minimax(0, False)
                # print("SCORE", score)
                self.board[index] = ' '
                if score > best_score:
                    best_score = score
                    best_move = index

        self.board[best_move] = "X" if self.player_turn == 1 else "O"
        print(f"Computer Player {self.player_turn} is making their move...")
        sleep(2)


    def minimax(self, depth, is_maximizing):
        """Recursive function to handle computer playing out all possible scenarios and 
        determining which has the best score"""

        # set up scores depending on which turn
        if self.player_turn == 1:
            scores = { "X": 10, "O": -10, 'tie': 0 }
        else:
            scores = { "X": -10, "O": 10, 'tie': 0 }

        result = self.check_for_win()
        # recursive base case
        if result != None:
            return scores[result]
        
        if is_maximizing:
            best_score = float("-inf")
            for index, move in enumerate(self.board):
                if move == ' ':
                    self.board[index] = "X" if self.player_turn == 1 else "O"
                    score = self.minimax(depth + 1, False)
                    self.board[index] = ' '
                    best_score = max(score, best_score)
            return best_score
        
        else:  #not maximizing
            best_score = float("inf")
            for index, move in enumerate(self.board):
                if move == ' ':
                    self.board[index] = "X" if self.player_turn == 2 else "O"
                    score = self.minimax(depth + 1, True)
                    self.board[index] = ' '
                    best_score = min(score, best_score)
            return best_score


    def check_for_win(self):
        """Method to check the board for a win"""
        for val in range(0, 9, 3):
            #check rows
            if self.board[val] == self.board[val + 1] == self.board[val + 2]:  
                if self.board[val] == "X":
                    return "X"
                elif self.board[val] == "O":
                    return "O"
                
        for val in range(3):
            #check columns
            if self.board[val] == self.board[val + 3] == self.board[val + 6]:  
                if self.board[val] == "X":
                    return "X"
                elif self.board[val] == "O":
                    return "O"
        
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]: 
            if self.board[4] == "X":
                return "X"
            elif self.board[4] == "O":
                return "O"
        
        # check for no more moves or tie game
        if ' ' not in self.board: 
            return "tie"
        
        return None
            

    def play_game(self):
        """Method to handle the game play"""
        os.system("cls")
        print(logo)
        print("Welcome to Tic Tac Toe!")
        self.player1 = self.set_player_type(1)
        print(f'Player1 is a {self.player1} and will play "X"')
        self.player2 = self.set_player_type(2)
        print(f'Player2 is a {self.player2} and will play "O"')
        sleep(2)

        while True:
            print_display(self.board)

            if self.player1 == "Human":
                self.human_move()
            else: 
                self.computer_move()

            print_display(self.board)
            result = self.check_for_win()
            if result == 'tie':
                print("Game ends in a TIE!")
                return
            
            if result == "X":
                print('Player1 "X" wins!')
                return
                # maybe make a "initiate_win" method?

            self.player_turn = 2
         
            if self.player2 == "Human":
                self.human_move()
            else: 
                self.computer_move()

            print_display(self.board)
            result = self.check_for_win()
            if result == 'tie':
                print("Game ends in a TIE!")
                return
            
            if result == "O":
                print('Player2 "O" wins!')
                return

            self.player_turn = 1
        


TicTacToe()


