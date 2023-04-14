import tkinter as tk


class Awale:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jeu de l'awalé")
        self.window.geometry("500x300")

        self.player1 = ["A", "A", "A", "A", "A", "A"]
        self.player2 = ["A", "A", "A", "A", "A", "A"]
        self.turn = 1

        self.draw_board()

    def draw_board(self):
        self.board_frame = tk.Frame(self.window, bg="tan")
        self.board_frame.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(6):
            tk.Label(self.board_frame, text=self.player1[i], font=(
                "Arial", 30)).grid(row=0, column=i)
            tk.Label(self.board_frame, text=self.player2[i], font=(
                "Arial", 30)).grid(row=1, column=i)

        self.status_label = tk.Label(
            self.window, text="Joueur 1 à vous de jouer", font=("Arial", 20))
        self.status_label.pack(pady=10)

        self.window.bind("<Button-1>", self.move)

    def move(self, event):
        x = event.x
        y = event.y

        if y < 150:
            player = self.player1
            opponent = self.player2
            row = 0
        else:
            player = self.player2
            opponent = self.player1
            row = 1

        col = x // 83

        if player[col] == " ":
            return

        seeds = player[col]
        player[col] = " "

        while seeds > 0:
            col = (col + 1) % 6

            if row == 0 and col == 0:
                continue
            if row == 1 and col == 5:
                continue

            player[col] += 1
            seeds -= 1

        if player == self.player1:
            self.turn = 2
        else:
            self.turn = 1

        if self.game_over():
            self.status_label.config(text="Jeu terminé!")
            return

        if self.turn == 1:
            self.status_label.config(text="Joueur 1 à vous de jouer")
        else:
            self.status_label.config(text="Joueur 2 à vous de jouer")

    def game_over(self):
        if sum(self.player1) == 0 or sum(self.player2) == 0:
            return True
        return False

    def run(self):
        self.window.mainloop()


game = Awale()
game.run()
