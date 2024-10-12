import copy

def check_draw(board):
  n = 5
  for i in range(n):
    for j in range(n):
      if board[i][j] == "":
        return False
  return True

def get_diags(board):
  all_diags = []
  dir_1_s = [(3, 0), (4, 0), (3, 1), (4, 1)]
  for i, j in dir_1_s:
    diag = []
    for _ in range(4):
      diag.append(board[i][j])
      i -= 1
      j += 1
    all_diags.append(diag)
      
  dir_2_s = [(0, 0), (0, 1), (1, 0), (1, 1)]
  for i, j in dir_2_s:
    diag = []
    for _ in range(4):
      diag.append(board[i][j])
      i += 1
      j += 1
    all_diags.append(diag)
  
  return all_diags

def check_win(board):
    n = 5
    for i in range(len(board)):
      for j in range(n - 4 + 1):
        if board[i][j:j+3] == ["X"] * 4:
          return "X"
        elif board[i][j:j+4] == ["O"] * 4:
          return "O"

    for j in range(n):
      for i in range(n - 4 + 1):
        col = [board[i+x][j] for x in range(4)]
        if col == ["X"] * 4:
          return "X"
        elif col == ["O"] * 4:
          return "O"
        
    for diag in get_diags(board):
      if diag == ["X"] * 4:
        return "X"
      elif diag == ["O"] * 4:
        return "O"

    return "-"

def space_score(row, p):
  if p == "O":
    q = "X"
  else:
    q = "O"

  if q in row or q.lower() in row:
    return 0
  
  count_p, count_p_lower = 0, 0
  for char in row:
    if char == p:
      count_p += 1
    if char == p.lower():
      count_p_lower += 1

  score = 0
  if count_p == 1:
    score = 3
  elif count_p == 2:
    score = 7
  elif count_p == 3:
    score = 15

  if p.lower() in row:
    score *= 1.1 ** count_p_lower

  return score
  

def eval_func(board, p):
  n = 5
  total_score = 0
  for i in range(5):
    for j in range(n - 4 + 1):
      total_score += space_score(board[i][j:j+4], p)

  for j in range(n):
    for i in range(n - 4 + 1):
      col = [board[i+x][j] for x in range(4)]
      total_score += space_score(col, p)

  for diag in get_diags(board):
    total_score += space_score(diag, p)

  return total_score / 300

def score(board, maximizingPlayer):
  if check_win(board) == "X":
    return 1
  
  if check_win(board) == "O":
    return -1 
  
  if check_draw(board):
    return 0
  
  if maximizingPlayer == "O":
    minimizingPlayer = "X"
  else:
    minimizingPlayer = "O"

  return eval_func(board, maximizingPlayer) - eval_func(board, minimizingPlayer)

def child_boards(board, player):
  children = []
  for i in range(5):
    for j in range(5):
      if board[i][j] == "" or board[i][j] == player.lower():
        child = copy.deepcopy(board)
        child[i][j] = player
        children.append(([i, j], child))
  return children

def alpha_beta_search(board, current_player):
    max_depth = 2
    return max_value(board, -float("inf"), float("inf"), current_player, 0, max_depth)

def max_value(board, alpha, beta, current_player, depth, max_depth):
    if check_draw(board) or check_win(board) != "-":
        return score(board, current_player), None
    
    v = -float("inf")
    for move, new_board in child_boards(board, current_player):
      if depth >= max_depth:
          v2, _ = score(new_board, current_player), move
      else:
          v2, _ = min_value(new_board, alpha, beta, current_player, depth + 1, max_depth)

      if v2 > v:
          v, best_move = v2, move
          alpha = max(alpha, v)

      if v >= beta:
          return v, best_move
    return v, best_move

def min_value(board, alpha, beta, current_player, depth, max_depth):
    if check_draw(board) or check_win(board) != "-":
        return score(board, current_player), None

    if current_player == "X":
      sim_player = "O"
    else:
      sim_player = "X"

    v = float("inf")
    for move, new_board in child_boards(board, sim_player):
      if depth >= max_depth:
          v2, _ = score(new_board, current_player), move
      else:
          v2, _ = max_value(new_board, alpha, beta, current_player, depth + 1, max_depth)

      if v2 < v:
          v, best_move = v2, move
          beta = min(beta, v)

      if v <= alpha:
            return v, best_move
    return v, best_move
    

    
