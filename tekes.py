from tkinter import *


class TekesGame:
    def __init__(self):
        self.board = [0] * 21
        for i in range(1, 21):
            self.board[i] = 3 if i in [
                1, 2, 3, 9, 10, 11, 12, 18, 19, 20] else 4
        self.player_turn = 0
        self.game_over = False

    def play(self, index):
        if not self.game_over:
            if self.player_turn == 0 and index in range(1, 10):
                if self.board[index] > 0:
                    self.board[index] -= 1
                    if self.board[index] == 0:
                        self.capture(index)
                    else:
                        self.player_turn = 1
            elif self.player_turn == 1 and index in range(11, 20):
                if self.board[index] > 0:
                    self.board[index] -= 1
                    if self.board[index] == 0:
                        self.capture(index)
                    else:
                        self.player_turn = 0

    def capture(self, index):
        opposite_index = 20 - index
        captured = self.board[opposite_index]
        self.board[opposite_index] = 0
        self.board[0] += captured + 1
        if sum(self.board[1:10]) == 0 or sum(self.board[11:20]) == 0:
            self.end_game()

    def end_game(self):
        self.game_over = True

    def score(self):
        score1 = self.board[0] + self.board[1] + \
            self.board[2] + self.board[3] + self.board[4]
        score2 = self.board[5] + self.board[6] + \
            self.board[7] + self.board[8] + self.board[9]
        return score1, score2


class TekesGUI:
    def __init__(self):
        self.tekes_game = TekesGame()

        self.window = Tk()
        self.window.title("Tekes Game")

        self.holes = []
        for i in range(19, 9, -1):
            button = Button(self.window, text=str(self.tekes_game.board[i]), width=4,
                            command=lambda i=i: self.play(i))
            button.grid(row=0, column=19-i)
            self.holes.append(button)

        self.score1 = Label(self.window, text="Score: 0")
        self.score1.grid(row=0, column=0)

        self.score2 = Label(self.window, text="Score: 0")
        self.score2.grid(row=0, column=18)

        self.turn_label = Label(self.window, text="Player 1's turn")
        self.turn_label.grid(row=1, column=0, columnspan=19)

        self.reset_button = Button(
            self.window, text="Reset", command=self.reset)
        self.reset_button.grid(row=2, column=0, columnspan=19)

    def play(self, index):
        self.tekes_game.play(index)
        self.update()

    def update(self):
        for i in range(19, 9, -1):
            self.holes[19-i].configure(text=str(self.tekes_game.board[i]))
        self.score1.configure(text="Score: " + str(self.tekes_game.board[0]))
        self.score2.configure(text="Score: " + str(self.tekes_game.board[20]))
        if self.tekes_game.game_over:
            score1, score2 = self.tekes_game.score()
            if score1 > score2:
                winner = "Player 1 wins!"
            elif score2 > score1:
                winner = "Player 2 wins!"
            else:
                winner = "It's a tie!"
            self.turn_label.configure(text=winner)
        else:
            if self.tekes_game.player_turn == 0:
                self.turn_label.configure(text="Player 1's turn")
            else:
                self.turn_label.configure(text="Player 2's turn")

    def reset(self):
        self.tekes_game = TekesGame()
        self.update()

    def run(self):
        self.window.mainloop()
