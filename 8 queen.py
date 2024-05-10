def safe_position(board, col):
  """
  Checks if a queen can be placed safely in a given column.
  """
  # Check for queens in the same row
  for row in range(len(board)):
    if board[row][col] == 1:
      return False

  # Check for queens diagonally
  row = col - 1
  diag = 1
  while row >= 0 and col - diag >= 0:
    if board[row][col - diag] == 1:
      return False
    row -= 1
    diag += 1

  row = col + 1
  diag = 1
  while row < len(board) and col + diag < len(board):
    if board[row][col + diag] == 1:
      return False
    row += 1
    diag += 1

  return True

def solve_n_queens(board, col):
  """
  Solves the N-Queens problem recursively using backtracking.
  """
  if col >= len(board):
    return True

  for row in range(len(board)):
    if safe_position(board, col):
      board[row][col] = 1
      if solve_n_queens(board, col + 1):
        return True
      board[row][col] = 0  # Backtrack

  return False

def print_board(board):
  """
  Prints the chessboard with Queens marked as 'Q' and empty squares as '.'
  """
  for row in board:
    for col in row:
      if col == 1:
        print("Q", end=" ")
      else:
        print(".", end=" ")
    print()

# Initialize an empty chessboard
board = [[0 for _ in range(8)] for _ in range(8)]

if solve_n_queens(board, 0):
  print("Solution Found:")
  print_board(board)
else:
  print("No solution exists")
