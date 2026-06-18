# first line: day and total steps
data1 = input().split()
day = int(data1[0]); total_step = int(data1[1])

# 2nd line: steps per day
data2_string = input().split()
data2 = []
for data in data2_string:
    data2.append(int(data))

# for saving the output
sol = []

# fewest day, start with only one day
for j in range(len(data2)):
    n = 1
    for i in range(len(data2)-j):
        step = 0; k = 0
        while k <= j:
            step += data2[i+k]
            k += 1
        # determine the step be chosen is enough or not
        if step >= total_step:
            sol.append([n, n+j, step])
        n += 1

if sol == []:
    # if no solution, print IMPOSSIBLE
    print("IMPOSSIBLE")
else:
    # show only the fewest day
    print(*sol[0])
