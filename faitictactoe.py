class TicTacToe:
    a = [" " for i in range(9)]

    def display(self):
        print("-"*13)
        print("|",self.a[0],"|",self.a[1],"|",self.a[2],"|")
        print("-"*13)
        print("|",self.a[3],"|",self.a[4],"|",self.a[5],"|")
        print("-"*13)
        print("|",self.a[6],"|",self.a[7],"|",self.a[8],"|")
        print("-"*13)
class players(TicTacToe):
    def __init__(self):
        self.player1 = input("Enter Player1 Name : ")
        self.player1_option = input("You X [or] O : ")
        self.player2 = input("Enter Player2 Name : ")
        self.player2_option = input("You X [or] O : ")
        print('*'*40,'\n','The Game Begins !\n','*'*39)

    def game_start(self):
        while True:
            player1_position = int(input("{} -- Enter Your Position : ".format(self.player1)))
            # self.check_player(player1_position)
            if self.a[player1_position-1] == " ":
                self.a[player1_position-1] = self.player1_option
                self.display()
                self.check = [
                (self.a[0], self.a[1], self.a[2]), (self.a[3],self. a[4], self.a[5]), (self.a[6], self.a[7], self.a[8]),
                (self.a[0], self.a[3], self.a[6]), (self.a[1],self. a[4], self.a[7]), (self.a[2], self.a[5], self.a[8]),
                (self.a[0], self.a[4], self.a[8]), (self.a[2],self. a[4], self.a[6])
                ]
                for chk in self.check:
                    if chk[0] == self.player1_option and chk[1] == self.player1_option and chk[2] == self.player1_option:
                        return "The Winner is -- {}".format(self.player1)
            else:
                print("Already Entered!\nTry another position")
            player2_position = int(input("{} -- Enter Your Position : ".format(self.player2)))
            if self.a[player2_position-1] == " ":
                self.a[player2_position-1] = self.player2_option
                self.display()
                self.check = [
                (self.a[0], self.a[1], self.a[2]), (self.a[3],self. a[4], self.a[5]), (self.a[6], self.a[7], self.a[8]),
                (self.a[0], self.a[3], self.a[6]), (self.a[1],self. a[4], self.a[7]), (self.a[2], self.a[5], self.a[8]),
                (self.a[0], self.a[4], self.a[8]), (self.a[2],self. a[4], self.a[6])
                ]
                for chk in self.check:
                    if chk[0] == self.player2_option and chk[1] == self.player2_option and chk[2] == self.player2_option:
                        return "The Winner is -- {}".format(self.player2)
            else:
                print("Already Entered!\nTry another position")
game = players()
print(game.game_start())
