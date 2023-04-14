import tkinter as tk


class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=5,
                                   command=lambda i=i, j=j: self.play_turn(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def play_turn(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win():
                self.show_winner()
            elif self.check_tie():
                self.show_tie()
            else:
                self.switch_player()

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def show_winner(self):
        winner = self.current_player
        self.disable_buttons()
        message = f"Le joueur {winner} gagne!"
        self.show_message(message)

    def check_tie(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def show_tie(self):
        self.disable_buttons()
        message = "Match nul!"
        self.show_message(message)

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def show_message(self, message):
        label = tk.Label(self.root, text=message, font=("Arial", 24))
        label.grid(row=3, column=0, columnspan=3)

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
