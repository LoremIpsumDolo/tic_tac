import os


class Player:

    def __init__(self, name: str):
        self.Name = name
        self.Score = 0



class Board:

    def __init__(self, player_1, player_2):
        self.Player_1 = player_1
        self.Player_2 = player_2
        self.CurrentBoard = self.reset_board()

    def print_board(self):
        os.system('clear')
        print(f"{self.Player_1.Name}: {self.Player_1.Score}")
        print(f"{self.Player_2.Name}: {self.Player_2.Score}")
        print("-----------------")
        for row in self.CurrentBoard.values():
            row_string = " | ".join(row)
            print(row_string)


    def reset_board(self) -> dict:
        return {
            1: ["O", " ", " "],
            2: [" ", "X", " "],
            3: ["O", " ", "X"]
        }


if __name__ == '__main__':

    game = Board(Player("Felix"),
                 Player("Feri"))

    game.print_board()
