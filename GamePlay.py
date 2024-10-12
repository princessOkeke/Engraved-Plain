import tkinter as tk
from tkmacosx import Button
import numpy as np
from minimax import alpha_beta_search

class GamePlay():
  def __init__(self, n, green, red):
    self.n = n
    self.green = green
    self.red = red
    self.board = [["" for i in range(self.n)] for i in range(self.n)]
    self.curr_player = "O"
    self.ai = "X"
    self.winner = "-"
    self.single_player = True

    root = tk.Tk()
    root.geometry("650x750")
    root.title("Engraved Plain")

    player_selection_frame = tk.Frame(root)
    player_selection_frame.columnconfigure(0, weight=1)
    player_selection_frame.columnconfigure(1, weight=1)

    self.single_button = Button(player_selection_frame, text="Single", font=('Arial', 16), 
                                bg="#E4F6F8", height=50, width=100, command=self.single)
    self.single_button.grid(row=0, column=0, sticky=tk.W+tk.E)

    self.dual_button = Button(player_selection_frame, text="Double", font=('Arial', 16), 
                              height=50, width=100, command=self.dual)
    self.dual_button.grid(row=0, column=1, sticky=tk.W+tk.E)

    player_selection_frame.pack(pady=30)

    buttonframe = tk.Frame(root)
    for i in range(5):
        buttonframe.columnconfigure(i, weight=1)

    self.buttons = {}
    for i in range(5):
        for j in range(5):
            btn = Button(
              buttonframe, 
              text="", 
              font=('Arial', 30), 
              height=80, 
              width=80, 
              command=lambda x=i, y=j: self.play(x, y))
            btn.grid(row=i, column=j, sticky=tk.W+tk.E)
            self.buttons[(i, j)] = btn
    
    buttonframe.pack(padx=20, pady=10)

    reset_button = Button(root, text="Reset", font=('Arial', 30), height=60, width=120, command=self.reset)
    reset_button.pack(pady=50)

    self.reset()
    root.mainloop()

  def single(self):
    self.single_player = True
    self.single_button.config(bg="#E4F6F8")
    self.dual_button.config(bg="white")
    self.reset()

  def dual(self):
    self.single_player = False
    self.single_button.config(bg="white")
    self.dual_button.config(bg="#E4F6F8")
    self.reset()

  def reset(self):
    self.board = [["" for i in range(self.n)] for i in range(self.n)]
    self.winner = "-"
    if self.single_player:
      self.curr_player = "O"
    else:
      self.curr_player = "X"

    for x in range(5):
      for y in range(5):
        btn = self.buttons[(x, y)]
        btn.config(bg="white", text="")

    n = 3
    spots = np.random.choice(range(1, 26), n*2, replace=False)
    g, r = spots[:n], spots[n:]
    self.green, self.red = [self.to_pos(num) for num in g], [to_pos(num) for num in r]

    for x, y in self.green:
      self.board[x][y] = "x"
      self.buttons[(x, y)].config(bg="#c1ffa7")

    for x, y in self.red:
      self.board[x][y] = "o"
      self.buttons[(x, y)].config(bg="#ff9580")

    if self.single_player:
      self.ai_play()
  
  def ai_play(self):
    _, move = alpha_beta_search(self.board, self.ai)
    if move:
      x, y = move
    else:
      num = np.random.choice(range(1, 26))
      x, y = self.to_pos(num)
      while not self.validate_move(x, y):
        num = np.random.choice(range(1, 26))
        x, y = self.to_pos(num)
  
    btn = self.buttons[(x, y)]
    if self.ai == "X":
      self.board[x][y] = "X"
      btn.config(text ="❎", bg="#c1ffa7")
    
    if self.ai == "O":
      self.board[x][y] = "O"
      btn.config(text = "🅾️", bg="#ff9580")

    self.winner, positions = self.check_win()
    if self.winner == self.ai:
      for i, j in positions:
        btn = self.buttons[(i, j)]
        btn.config(text ="🏆", bg="gold")


  def play(self, x, y):
    if self.winner == "X" or self.winner == "O":
      self.reset()
      return

    if not self.validate_move(x, y):
      return

    btn = self.buttons[(x, y)]
    if self.curr_player == "X":
      self.board[x][y] = "X"
      btn.config(text ="❎", bg="#c1ffa7")
    
    if self.curr_player == "O":
      self.board[x][y] = "O"
      btn.config(text = "🅾️", bg="#ff9580")

    self.winner, positions = self.check_win()
    if self.winner == self.curr_player:
      for i, j in positions:
        btn = self.buttons[(i, j)]
        btn.config(text ="🏆", bg="gold")
    else:
      if self.single_player:
        self.ai_play()
      else:
        if self.curr_player == "X":
          self.curr_player = "O"
        elif self.curr_player == "O":
          self.curr_player = "X"

  def validate_move(self, x, y):
    if self.board[x][y] == "":
      return True

    if self.curr_player == "X" and self.board[x][y] == "x":
      return True

    if self.curr_player == "O" and self.board[x][y] == "o":
      return True

    return False
  
  def get_diags(self):
    all_diags = []
    all_diags_pos = []
    dir_1_s = [(3, 0), (4, 0), (3, 1), (4, 1)]
    for i, j in dir_1_s:
      diag = []
      diag_pos = []
      for _ in range(4):
        diag.append(self.board[i][j])
        diag_pos.append((i, j))
        i -= 1
        j += 1
      all_diags.append(diag)
      all_diags_pos.append(diag_pos)
        
    dir_2_s = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for i, j in dir_2_s:
      diag = []
      diag_pos = []
      for _ in range(4):
        diag.append(self.board[i][j])
        diag_pos.append((i, j))
        i += 1
        j += 1
      all_diags.append(diag)
      all_diags_pos.append(diag_pos)
    
    return all_diags, all_diags_pos

  def check_win(self):
    for i in range(len(self.board)):
      for j in range(self.n - 4 + 1):
        if self.board[i][j:j+4] == ["X"] * 4:
          return "X", [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]
        elif self.board[i][j:j+4] == ["O"] * 4:
          return "O", [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)]

    for j in range(self.n):
      for i in range(self.n - 4 + 1):
        col = [self.board[i+x][j] for x in range(4)]
        if col == ["X"] * 4:
          return "X", [(i, j), (i + 1, j), (i + 2, j), (i + 3, j)]
        elif col == ["O"] * 4:
          return "O", [(i, j), (i + 1, j), (i + 2, j), (i + 3, j)]
        
    diags, diags_pos = self.get_diags();
    for i in range(len(diags)):
      if diags[i] == ["X"] * 4:
        return "X", diags_pos[i]
      elif diags[i] == ["O"] * 4:
        return "O", diags_pos[i]

    return "-", []
  
  def to_pos(self, num):
    return (num-1) // 5, (num-1) % 5
  
def to_pos(num):
  return (num-1) // 5, (num-1) % 5

if __name__ == "__main__":
  game = GamePlay(5, [], [])