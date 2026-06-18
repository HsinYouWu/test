# # Read the number of rows and columns
# rows = int(input())
# cols = int(input())

# # Create the board with all cells initialized to 0
# board = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(0)
#     board.append(row)

# # Read the mine indices as a string and split by '|'
# mine_input = input()
# mine_parts = mine_input.split('|')

# # Store valid mine positions
# valid_mines = []

# # Check each mine index
# for part in mine_parts:
#     idx = int(part)

#     # If the index is invalid, print the warning message
#     if idx < 0 or idx >= rows * cols:
#         print(f"Invalid index: {idx}")
#     else:
#         # Convert linear index to row and column
#         r = idx // cols
#         c = idx % cols

#         # Avoid placing the same mine repeatedly
#         if (r, c) not in valid_mines:
#             valid_mines.append((r, c))
#             board[r][c] = '*'

# # Directions for 8 neighboring cells
# directions = [
#     (-1, -1), (-1, 0), (-1, 1),
#     (0, -1),           (0, 1),
#     (1, -1),  (1, 0),  (1, 1)
# ]

# # Fill each non-mine cell with the number of adjacent mines
# for r in range(rows):
#     for c in range(cols):
#         if board[r][c] != '*':
#             count = 0

#             for dr, dc in directions:
#                 nr = r + dr
#                 nc = c + dc

#                 # Check boundary and whether the neighbor is a mine
#                 if 0 <= nr < rows and 0 <= nc < cols:
#                     if board[nr][nc] == '*':
#                         count += 1

#             board[r][c] = count

# # Display the final board
# for r in range(rows):
#     for c in range(cols):
#         print(board[r][c], end=' ')
#     print()

#------------------------------------------------------
row_and_col = input()
row = int(row_and_col.split()[0])
col = int(row_and_col.split()[1])

mine = input().split("|")

mine_list = []
i = 0
while i < len(mine):
    index = int(mine[i])
    if index < 0 or index >= row * col:
        print(f"Invalid index: {index}")
    else:
        mine_list.append(index)
    i += 1

board = []
k1 = 0
while k1 < row:
    board.append([])
    k2 = 0
    while k2 < col:
        board[k1].append("_")
        k2 += 1
    k1 += 1

j = 0
while j < len(mine_list):
    index = mine_list[j]
    row_index = index // col
    col_index = index % col
    board[row_index][col_index] = "*"
    j += 1

m = 0
while m < row:
    n = 0
    while n < col:
        num = 0
        if board[m][n] != "*":
            if 1 <= m and 1 <= n and board[m-1][n-1] == "*":
                num += 1
            if m <= row-2 and 1 <= n and board[m+1][n-1] == "*":
                num += 1
            if 1 <= m and n <= col-2 and board[m-1][n+1] == "*":
                num += 1
            if m <= row-2 and n <= col-2 and board[m+1][n+1] == "*":
                num += 1
            if 1 <= m and board[m-1][n] == "*":
                num += 1
            if m <= row-2 and board[m+1][n] == "*":
                num += 1
            if 1 <= n and board[m][n-1] == "*":
                num += 1
            if n <= col-2 and board[m][n+1] == "*":
                num += 1
            board[m][n] = str(num)
        n += 1
    m += 1

m = 0
while m < len(board):
    print(*board[m])
    m += 1