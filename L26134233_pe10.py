import curses
import random
import time


# Symbols used in the game
SNAKE_HEAD = "O"
SNAKE_BODY = "o"
NORMAL_FOOD = "π"
SPECIAL_FOOD = "X"
EMPTY_CELL = " "


def place_random_cell(height, width, forbidden):
    """Return a random (y, x) position that is not in forbidden."""
    while True:
        y = random.randint(1, height - 2)
        x = random.randint(1, width - 2)
        if (y, x) not in forbidden:
            return (y, x)


def generate_obstacles(height, width, snake):
    """
    Generate obstacles occupying about 5% of the screen.
    Each obstacle segment has at least 5 consecutive cells,
    arranged either horizontally or vertically.
    """
    obstacles = set()
    target_count = max(5, int(height * width * 0.05))
    snake_set = set(snake)
    max_attempts = 5000
    attempts = 0

    while len(obstacles) < target_count and attempts < max_attempts:
        attempts += 1
        length = random.randint(5, 10)
        direction = random.choice(["horizontal", "vertical"])

        if direction == "horizontal":
            y = random.randint(1, height - 2)
            x = random.randint(1, max(1, width - length - 2))
            cells = [(y, x + i) for i in range(length)]
        else:
            y = random.randint(1, max(1, height - length - 2))
            x = random.randint(1, width - 2)
            cells = [(y + i, x) for i in range(length)]

        # Keep the initial snake area safe and avoid overlapping existing obstacles.
        if all(
            1 <= cy < height - 1
            and 1 <= cx < width - 1
            and (cy, cx) not in snake_set
            and (cy, cx) not in obstacles
            for cy, cx in cells
        ):
            obstacles.update(cells)

    return obstacles


def draw_border(stdscr, height, width):
    """Draw a simple border around the game area."""
    try:
        stdscr.border()
    except curses.error:
        pass


def draw_game(stdscr, height, width, snake, obstacles, normal_food, special_food,
              normal_count, special_count, paused):
    """Draw all game objects on the screen."""
    stdscr.erase()
    draw_border(stdscr, height, width)

    # Status line
    status = f" Normal: {normal_count} | Special: {special_count} | SPACE: pause/resume | q: quit "
    if paused:
        status += " | PAUSED "
    try:
        stdscr.addstr(0, 2, status[:width - 4])
    except curses.error:
        pass

    # Draw obstacles with inverted colors.
    for y, x in obstacles:
        try:
            stdscr.addstr(y, x, " ", curses.A_REVERSE)
        except curses.error:
            pass

    # Draw food.
    try:
        stdscr.addstr(normal_food[0], normal_food[1], NORMAL_FOOD)
        stdscr.addstr(special_food[0], special_food[1], SPECIAL_FOOD)
    except curses.error:
        pass

    # Draw snake.
    for i, (y, x) in enumerate(snake):
        try:
            if i == 0:
                stdscr.addstr(y, x, SNAKE_HEAD)
            else:
                stdscr.addstr(y, x, SNAKE_BODY)
        except curses.error:
            pass

    stdscr.refresh()


def show_game_over(stdscr, height, width, normal_count, special_count, reason):
    """Display final result when the game ends."""
    stdscr.erase()
    messages = [
        "GAME OVER",
        f"Normal food eaten : {normal_count}",
        f"Special food eaten: {special_count}",
        f"Reason: {reason}",
        "Press any key to exit."
    ]

    start_y = max(1, height // 2 - len(messages) // 2)
    for i, msg in enumerate(messages):
        x = max(1, (width - len(msg)) // 2)
        try:
            stdscr.addstr(start_y + i, x, msg)
        except curses.error:
            pass

    stdscr.refresh()
    stdscr.nodelay(False)
    stdscr.getch()


def run_game(stdscr):
    """Main game loop."""
    curses.curs_set(0)          # Hide cursor
    stdscr.nodelay(True)        # Non-blocking keyboard input
    stdscr.keypad(True)         # Enable arrow keys

    # Get terminal size and leave a minimum playable area.
    height, width = stdscr.getmaxyx()
    if height < 12 or width < 30:
        stdscr.nodelay(False)
        stdscr.addstr(0, 0, "Terminal window is too small. Please enlarge it and run again.")
        stdscr.getch()
        return

    # Initial snake: 3 units long and moving right.
    start_y = height // 2
    start_x = width // 2
    snake = [
        (start_y, start_x),
        (start_y, start_x - 1),
        (start_y, start_x - 2)
    ]

    direction = (0, 1)          # right
    next_direction = direction
    delay = 0.15                # snake speed; smaller means faster
    min_delay = 0.05

    normal_count = 0
    special_count = 0
    paused = False
    reason = ""

    obstacles = generate_obstacles(height, width, snake)

    forbidden = set(snake) | obstacles
    normal_food = place_random_cell(height, width, forbidden)
    forbidden.add(normal_food)
    special_food = place_random_cell(height, width, forbidden)

    while True:
        key = stdscr.getch()

        # Keyboard controls.
        if key == ord("q") or key == ord("Q"):
            reason = "Player quit the game."
            break
        elif key == ord(" "):
            paused = not paused
        elif key == curses.KEY_UP and direction != (1, 0):
            next_direction = (-1, 0)
            delay = max(min_delay, delay * 0.97)  # accelerate a little bit
        elif key == curses.KEY_DOWN and direction != (-1, 0):
            next_direction = (1, 0)
            delay = max(min_delay, delay * 0.97)
        elif key == curses.KEY_LEFT and direction != (0, 1):
            next_direction = (0, -1)
            delay = max(min_delay, delay * 0.97)
        elif key == curses.KEY_RIGHT and direction != (0, -1):
            next_direction = (0, 1)
            delay = max(min_delay, delay * 0.97)

        if paused:
            draw_game(stdscr, height, width, snake, obstacles, normal_food, special_food,
                      normal_count, special_count, paused)
            time.sleep(0.05)
            continue

        direction = next_direction
        head_y, head_x = snake[0]
        dy, dx = direction

        # Wrap around inside the border.
        new_y = head_y + dy
        new_x = head_x + dx
        if new_y <= 0:
            new_y = height - 2
        elif new_y >= height - 1:
            new_y = 1
        if new_x <= 0:
            new_x = width - 2
        elif new_x >= width - 1:
            new_x = 1

        new_head = (new_y, new_x)

        # Collision with obstacles.
        if new_head in obstacles:
            reason = "The snake collided with an obstacle."
            break

        # Collision with itself.
        # The current tail is allowed to move away unless the snake is eating normal food.
        eating_normal = new_head == normal_food
        eating_special = new_head == special_food
        body_to_check = snake if eating_normal else snake[:-1]
        if new_head in body_to_check:
            reason = "The snake collided with itself."
            break

        # Move snake.
        snake.insert(0, new_head)

        if eating_normal:
            # Do not remove tail, so the snake grows by 1.
            normal_count += 1
            forbidden = set(snake) | obstacles | {special_food}
            normal_food = place_random_cell(height, width, forbidden)
        elif eating_special:
            special_count += 1
            # Normal movement removes one tail. Special food removes one extra tail,
            # but the snake cannot shrink if its length is less than or equal to 1.
            snake.pop()
            if len(snake) > 1:
                snake.pop()
            forbidden = set(snake) | obstacles | {normal_food}
            special_food = place_random_cell(height, width, forbidden)
        else:
            # Normal movement: remove tail.
            snake.pop()

        draw_game(stdscr, height, width, snake, obstacles, normal_food, special_food,
                  normal_count, special_count, paused)
        time.sleep(delay)

    show_game_over(stdscr, height, width, normal_count, special_count, reason)


if __name__ == "__main__":
    curses.wrapper(run_game)
