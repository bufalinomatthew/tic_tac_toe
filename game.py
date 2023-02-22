import random

class game_play: 
    def __init__(self):
        self.board_list = [1,2,3,4,5,6,7,8,9]
        self.board = f'''
                 |     |     
              {self.board_list[0]}  |  {self.board_list[1]}  |  {self.board_list[2]}  
            _____|_____|_____
                 |     |     
              {self.board_list[3]}  |  {self.board_list[4]}  |  {self.board_list[5]}  
            _____|_____|_____
                 |     |     
              {self.board_list[6]}  |  {self.board_list[7]}  |  {self.board_list[8]}  
                 |     |     
            '''

        pass
    def __str__(self):
        intro = f'''
            Welcom to Tic Tac Toe!! 

            Here is your Game Board
            {self.board}


            '''
        return intro

    def ready_to_play(self):
        ready = input("Are you ready to play? y/n \n")
        self.num_players = int(input("How many players: (enter 1 or 2)\n"))

        if((ready == 'y') & (self.num_players == 2)):
            self.player1 = input("Player 1 name: ")
            self.player2 = input("Player 2 name: ")

            print(f"{self.player1} you are X\n")
            print(f"{self.player2} you are O\n\n")
        elif((ready == 'y') & (self.num_players == 1)):
            self.player1 = input("Player 1 name: ")

            print(f"{self.player1} you are X\n")
            print(f"Computer will play O\n\n")
        else: 
            print('please let me know when you want to play')

    def draw(self):
        self.board = f'''
                 |     |     
              {self.board_list[0]}  |  {self.board_list[1]}  |  {self.board_list[2]}  
            _____|_____|_____
                 |     |     
              {self.board_list[3]}  |  {self.board_list[4]}  |  {self.board_list[5]}  
            _____|_____|_____
                 |     |     
              {self.board_list[6]}  |  {self.board_list[7]}  |  {self.board_list[8]}  
                 |     |     
            '''
        print(self.board)
        return self.board
    
    def win_condition(self):
        if ((self.board_list[0] == 'X') & ((self.board_list[1] == 'X')) & (self.board_list[2] == 'X')) | ((self.board_list[0] == 'O') & ((self.board_list[1] == 'O')) & (self.board_list[2] == 'O')): 
            if ((self.board_list[0] == 'X') & ((self.board_list[1] == 'X')) & (self.board_list[2] == 'X')):
                print(f"Winner {self.player1}!")
            else: 
                try: 
                    print(f"Winner {self.player2}!")
                except: 
                    print("Computer won!")
            return True
        elif ((self.board_list[3] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[5] == 'X')) | ((self.board_list[3] == 'O') & ((self.board_list[4] == 'O')) & (self.board_list[5] == 'O')):
            if ((self.board_list[3] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[5] == 'X')):
                print(f"Winner {self.player1}!")
            else: 
                try: 
                    print(f"Winner {self.player2}!")
                except: 
                    print("Computer won!")
            return True
        elif ((self.board_list[6] == 'X') & ((self.board_list[7] == 'X')) & (self.board_list[8] == 'X')) | ((self.board_list[6] == 'O') & ((self.board_list[7] == 'O')) & (self.board_list[8] == 'O')):
            if ((self.board_list[6] == 'X') & ((self.board_list[7] == 'X')) & (self.board_list[8] == 'X')):
                print(f"Winner {self.player1}!")
            else: 
                try: 
                    print(f"Winner {self.player2}!")
                except: 
                    print("Computer won!")
            return True
        elif ((self.board_list[0] == 'X') & ((self.board_list[3] == 'X')) & (self.board_list[6] == 'X')) | ((self.board_list[0] == 'O') & ((self.board_list[3] == 'O')) & (self.board_list[6] == 'O')):
            if ((self.board_list[0] == 'X') & ((self.board_list[3] == 'X')) & (self.board_list[6] == 'X')):
                print(f"Winner {self.player1}!")
            else: 
                try: 
                    print(f"Winner {self.player2}!")
                except: 
                    print("Computer won!")
            return True
        elif ((self.board_list[1] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[7] == 'X')) | ((self.board_list[1] == 'O') & ((self.board_list[4] == 'O')) & (self.board_list[7] == 'O')):
            if ((self.board_list[1] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[7] == 'X')) :
                print(f"Winner {self.player1}!")
            else: 
                print(f"Winner {self.player2}!")
            return True
        elif ((self.board_list[2] == 'X') & ((self.board_list[5] == 'X')) & (self.board_list[8] == 'X')) | ((self.board_list[2] == 'O') & ((self.board_list[5] == 'O')) & (self.board_list[8] == 'O')):
            if ((self.board_list[2] == 'X') & ((self.board_list[5] == 'X')) & (self.board_list[8] == 'X')) :
                print(f"Winner {self.player1}!")
            else: 
                try: 
                    print(f"Winner {self.player2}!")
                except: 
                    print("Computer won!")
            return True
        elif ((self.board_list[0] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[8] == 'X')) | ((self.board_list[0] == 'O') & ((self.board_list[4] == 'O')) & (self.board_list[8] == 'O')):
            if ((self.board_list[0] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[8] == 'X')):
                print(f"Winner {self.player1}!")
            else: 
                try: 
                    print(f"Winner {self.player2}!")
                except: 
                    print("Computer won!")
            return True
        elif ((self.board_list[2] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[6] == 'X')) | ((self.board_list[2] == 'O') & ((self.board_list[4] == 'O')) & (self.board_list[6] == 'O')):
            if ((self.board_list[2] == 'X') & ((self.board_list[4] == 'X')) & (self.board_list[6] == 'X')):
                print(f"Winner {self.player1}!")
            else: 
                try: 
                    print(f"Winner {self.player2}!")
                except: 
                    print("Computer won!")
            return True
        else:
            return False

    def play(self):
        status = False
        if self.num_players == 2:
            while status == False:
                if (
                    (type(self.board_list[0]) == str) & 
                    (type(self.board_list[1]) == str) & 
                    (type(self.board_list[2]) == str) & 
                    (type(self.board_list[3]) == str) & 
                    (type(self.board_list[4]) == str) & 
                    (type(self.board_list[5]) == str) & 
                    (type(self.board_list[6]) == str) & 
                    (type(self.board_list[7]) == str) & 
                    (type(self.board_list[8]) == str)):
                    print("There are no more moves! the game ends in a draw")
                    status = True
                else:
                    player1_turn = int(input(f"{self.player1} where would you like to place your X: ")) -1
                    if type(self.board_list[player1_turn]) == str:
                        player1_turn = input(f"That space is taken, please choose another: ")
                    else: 
                        self.board_list[player1_turn] = 'X'
                        self.draw()
                        status = self.win_condition()

                    player2_turn = int(input(f"{self.player2} where would you like to place your O: ")) - 1
                    if type(self.board_list[player2_turn]) == str:
                        player1_turn = input(f"That space is taken, please choose another: ")
                    else: 
                        self.board_list[player2_turn] = 'O'
                        self.draw()
                        status = self.win_condition()
        elif self.num_players == 1:
            while status == False:
                if (
                    (type(self.board_list[0]) == str) & 
                    (type(self.board_list[1]) == str) & 
                    (type(self.board_list[2]) == str) & 
                    (type(self.board_list[3]) == str) & 
                    (type(self.board_list[4]) == str) & 
                    (type(self.board_list[5]) == str) & 
                    (type(self.board_list[6]) == str) & 
                    (type(self.board_list[7]) == str) & 
                    (type(self.board_list[8]) == str)):
                    print("There are no more moves! the game ends in a draw")
                    status = False
                else:
                    player1_turn = int(input(f"{self.player1} where would you like to place your X: ")) -1
                    if type(self.board_list[player1_turn]) == str:
                        player1_turn = input(f"That space is taken, please choose another: ")
                    else: 
                        self.board_list[player1_turn] = 'X'
                        status = self.win_condition()
                        if status: 
                            self.draw()
                            break
                    

                    computer = True    
                    while computer:
                        player2_turn = random.randrange(9)
                        if type(self.board_list[player2_turn]) == str:
                            computer = True
                        else: 
                            computer = False
                    self.board_list[player2_turn] = 'O'
                    self.draw()
                    status = self.win_condition()


game = game_play()
print(game)

game.ready_to_play()
game.play()

