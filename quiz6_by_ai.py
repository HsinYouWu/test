# first line: day and total steps
data1 = input().split()
day = int(data1[0])
total_step = int(data1[1])

# 2nd line: steps per day
data2_string = input().split()
data2 = []
for data in data2_string:
    data2.append(int(data))

# for saving the best output
best = []

# try from fewest days
for j in range(len(data2)):
    sol = []

    for i in range(len(data2) - j):
        step = 0
        k = 0

        # calculate total steps from day i to day i+j
        while k <= j:
            step += data2[i + k]
            k += 1

        # determine whether this period is enough or not
        if step >= total_step:
            sol.append([i + 1, i + j + 1, step])

    # if this length has answers, choose the one with smaller total steps
    if sol != []:
        best = sol[0]

        for ans in sol:
            if ans[2] < best[2]:
                best = ans

        break

if best == []:
    # if no solution, print IMPOSSIBLE
    print("IMPOSSIBLE")
else:
    print(*best)