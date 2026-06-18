row_and_col = input()
row = int(row_and_col.split()[0])
col = int(row_and_col.split()[1])

mine =  input().split("|")

mine_list = []
i = 0
while i < len(mine):
    if not mine[i].isdigit():
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
print(board)

# m, n = 0, 0
# while m < row:
#     while n < col:
