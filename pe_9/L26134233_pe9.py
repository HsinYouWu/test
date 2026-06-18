import random

def generate_path(N, M):
    # This function generates a random path through an NxM maze.
    # The maze is a dictionary. Key: (i, j), Value: 0 empty, 1 obstacle, 2 path.
    try:
        maze = {}

        # First, set every cell to empty.
        for i in range(N):
            for j in range(M):
                maze[(i, j)] = 0

        # Start from the top-left cell.
        i = 0
        j = 0
        maze[(i, j)] = 2

        # Move only right or down until reaching the bottom-right cell.
        while i != N - 1 or j != M - 1:
            if i == N - 1:
                # If already at the last row, can only move right.
                j = j + 1
            elif j == M - 1:
                # If already at the last column, can only move down.
                i = i + 1
            else:
                # Otherwise, randomly choose to move down or right.
                direction = random.choice(["down", "right"])
                if direction == "down":
                    i = i + 1
                else:
                    j = j + 1

            maze[(i, j)] = 2

        return maze

    except TypeError:
        print("TypeError occurred in generate_path function.")
        return {}
    except KeyError:
        print("KeyError occurred in generate_path function.")
        return {}


def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles to empty cells.
    try:
        count = 0

        # Keep trying until enough obstacles are added.
        while count < min_obstacles:
            i = random.randint(0, N - 1)
            j = random.randint(0, M - 1)

            # Only empty cells can become obstacles.
            if maze[(i, j)] == 0:
                maze[(i, j)] = 1
                count = count + 1

        return maze

    except KeyError:
        print("KeyError occurred in add_obstacles function.")
        return maze


def set_obstacle(maze, N, M):
    # This function allows the user to manually set an obstacle.
    # It keeps asking for coordinates until an obstacle is successfully placed.
    while True:
        try:
            coord = input("Enter the coordinate to set an obstacle (i,j): ")
            parts = coord.split(",")

            # The input must have two numbers.
            if len(parts) != 2:
                raise ValueError("Need to be coordinates.")

            i = int(parts[0])
            j = int(parts[1])

            # Check if the coordinate is inside the maze.
            if i < 0 or i >= N or j < 0 or j >= M:
                raise KeyError("Invalid coordinates. Please input coordinates within the range.")

            # Cannot set an obstacle on the path.
            if maze[(i, j)] == 2:
                print("Obstacle cannot be placed on the path.")
            # Cannot set an obstacle if one already exists.
            elif maze[(i, j)] == 1:
                print("Obstacle already exists at this location.")
            else:
                maze[(i, j)] = 1
                print("Obstacle placed at (" + str(i) + ", " + str(j) + ")")
                break

        except ValueError as error:
            print("ValueError in set_obstacle function. " + str(error))
        except KeyError as error:
            print("KeyError in set_obstacle function. " + str(error))


def remove_obstacle(maze, N, M):
    # This function allows the user to manually remove an obstacle.
    # It keeps asking for coordinates until an obstacle is successfully removed.
    while True:
        try:
            coord = input("Enter the coordinate to remove an obstacle (i,j): ")
            parts = coord.split(",")

            # The input must have two numbers.
            if len(parts) != 2:
                raise ValueError("Need to be coordinates.")

            i = int(parts[0])
            j = int(parts[1])

            # Check if the coordinate is inside the maze.
            if i < 0 or i >= N or j < 0 or j >= M:
                raise KeyError("Invalid coordinates. Please input coordinates within the range.")

            # Cannot remove a path cell.
            if maze[(i, j)] == 2:
                print("Obstacle does not exist on the path.")
            # Cannot remove if there is no obstacle.
            elif maze[(i, j)] == 0:
                print("Obstacle does not exist at this location.")
            else:
                maze[(i, j)] = 0
                print("Obstacle removed at (" + str(i) + ", " + str(j) + ")")
                break

        except ValueError as error:
            print("ValueError in remove_obstacle function. " + str(error))
        except KeyError as error:
            print("KeyError in remove_obstacle function. " + str(error))


def print_maze(maze, N, M):
    # This function prints the current maze.
    try:
        print("Generated Maze Map:")

        line = "+---" * M + "+"

        for i in range(N):
            print(line)
            row = "|"
            for j in range(M):
                if maze[(i, j)] == 0:
                    row = row + "   |"
                elif maze[(i, j)] == 1:
                    row = row + " X |"
                elif maze[(i, j)] == 2:
                    row = row + " O |"
            print(row)

        print(line)

    except KeyError:
        print("KeyError occurred in print_maze function.")


def main():
    # This function is the main driver of the program.
    try:
        # Read the maze blueprint file.
        while True:
            try:
                file_name = input("Enter file name: ")
                file = open(file_name, "r")
                lines = file.readlines()
                file.close()
                break
            except IOError:
                print("IOError occurred in main function. File not found. Please enter a valid file name.")

        # Count the number of rows and columns from the blueprint.
        N = 0
        M = 0

        for line in lines:
            if line.startswith("|"):
                N = N + 1
                if M == 0:
                    M = line.count("|") - 1

        # Ask for a valid number of obstacles.
        while True:
            try:
                min_obstacles = int(input(f"Enter the minimum number of obstacles (0-{(M-1)*(N-1)}): "))

                # Use N * M as the upper bound, but path cells cannot have obstacles.
                if min_obstacles < 0 or min_obstacles > (M - 1) * (N - 1):
                    raise ValueError("Invalid number of obstacles.")

                break
            except ValueError as error:
                print("ValueError occurred in main function. " + str(error))

        # Generate the maze and add obstacles.
        maze = generate_path(N, M)
        maze = add_obstacles(maze, min_obstacles, N, M)

        # Menu loop.
        while True:
            print("Options:")
            print("1. Set obstacle")
            print("2. Remove Obstacle")
            print("3. Print Maze")
            print("4. Exit")

            try:
                option = int(input("Enter your option: "))

                if option == 1:
                    set_obstacle(maze, N, M)
                elif option == 2:
                    remove_obstacle(maze, N, M)
                elif option == 3:
                    print_maze(maze, N, M)
                elif option == 4:
                    break
                else:
                    raise NameError("Invalid option. Please choose a valid option.")

            except ValueError:
                print("Invalid option. Please choose a valid option.")
            except NameError as error:
                print(error)

    except NameError:
        print("NameError occurred in main function.")


main()
