row_and_col = input()
row = int(row_and_col.split()[0])
col = int(row_and_col.split()[1])

mine =  input().split("|")

mine_list = []
i = 0
while i < len(mine):
    if not mine[i].isdigit():
        print(f"Invalid index: {mine[i]}")
    elif mine[i].isdigit() and int(mine[i]) >= row*col:
        print(f"Invalid index: {mine[i]}")
    else:
        mine_list.append(int(mine[i]))
    i += 1

board = []
k1, k2 = 0, 0
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
# print(board)

m, n = 0, 0
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
            board[m][n] = f"{num}"
        n += 1
    m += 1

m = 0
while m < len(board):
    print(*board[m])
    m += 1