import pygame
import random

# ================================
# Initialization
# ================================
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colours
DAY_SKY_COLOR = (135, 206, 235)
NIGHT_SKY_COLOR = (25, 25, 112)
GROUND_COLOR = (139, 69, 19)
ROAD_COLOR = (50, 50, 50)
ROAD_LINE_COLOR = (255, 255, 255)
TREE_TRUNK = (101, 67, 33)
TREE_LEAF = (139, 69, 19)
ORANGE = (255, 165, 0)
RED = (255, 69, 0)
YELLOW = (255, 255, 0)
HOUSE_COLOR = (150, 111, 51)
ROOF_COLOR = (100, 40, 40)
WINDOW_COLOR = (240, 230, 140)
STAR_COLOR = (255, 255, 255)
CAR_COLOR_DAY = (255, 0, 0)
CAR_COLOR_NIGHT = (0, 0, 255)

# Positions of houses and trees
house_positions = [(WIDTH // 2 - 300, HEIGHT - 250),(WIDTH // 2 - 100, HEIGHT - 250),(WIDTH // 2 + 100, HEIGHT - 250),(WIDTH // 2 + 300, HEIGHT - 250)]
trees = [(50, HEIGHT - 180),(750, HEIGHT - 180),(300, HEIGHT - 180),(500, HEIGHT - 180)]

# Random star positions
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT // 2)) for _ in range(30)]

# Initial positions for the sun and moon
sun_position = [-50, HEIGHT // 4]
moon_position = [-50, HEIGHT // 4]

# Car positions and speed
car_position_day = [-100, HEIGHT - 70]
car_position_night = [WIDTH + 100, HEIGHT - 70]
car_speed = 6

# Leaves falling animation
leaves = [[trees[0][0] + 5, HEIGHT - 150, ORANGE, 1.0],
[trees[1][0] + 10, HEIGHT - 160, RED, 1.2],
[trees[2][0] + 15, HEIGHT - 155, YELLOW, 1.1],
[trees[3][0] + 20, HEIGHT - 145, ORANGE, 1.0],
[trees[0][0] + 25, HEIGHT - 155, RED, 1.3],
[trees[1][0] + 30, HEIGHT - 150, YELLOW, 1.0],
[trees[2][0] + 35, HEIGHT - 140, ORANGE, 1.2],
[trees[3][0] + 40, HEIGHT - 155, RED, 1.1],
[trees[0][0] + 45, HEIGHT - 150, YELLOW, 1.0],
[trees[1][0] + 50, HEIGHT - 160, ORANGE, 1.3]]

# Game clock for frame control
clock = pygame.time.Clock()
frame_count = 0
is_day = True

# ================================
# Main Game Loop
# ================================
running = True
while running:
    frame_count += 1

    # Handle day/night logic
    if is_day:
        sun_position[0] += car_speed
        car_position_day[0] += car_speed
        
        if car_position_day[0] >= WIDTH:
            car_position_day[0] = -100
            is_day = False
            sun_position[0] = -50
            moon_position[0] = WIDTH + 50
    else:
        moon_position[0] -= car_speed
        car_position_night[0] -= car_speed
        
        if car_position_night[0] <= -100:
            car_position_night[0] = WIDTH + 100
            is_day = True
            sun_position[0] = -50
            moon_position[0] = WIDTH + 50

    # Falling leaves animation
    for leaf in leaves:
        leaf[1] += leaf[3]  # Fall speed
        if leaf[1] > HEIGHT - 100:
            leaf[1] = random.randint(HEIGHT - 200, HEIGHT - 150)

    # ================================
    # Drawing Functions
    # ================================
    screen.fill(DAY_SKY_COLOR if is_day else NIGHT_SKY_COLOR)
    pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - 100, WIDTH, 100))

    # Draw houses
    for i in range(4):
        x, y = house_positions[i]
        pygame.draw.rect(screen, HOUSE_COLOR, (x, y, 150, 150))
        pygame.draw.polygon(screen, ROOF_COLOR, [(x - 20, y), (x + 170, y), (x + 75, y - 70)])
        window_color = WINDOW_COLOR if is_day or frame_count % 30 < 15 else (30, 30, 30)
        pygame.draw.rect(screen, window_color, (x + 25, y + 30, 30, 30))
        pygame.draw.rect(screen, window_color, (x + 90, y + 30, 30, 30))
        pygame.draw.rect(screen, TREE_TRUNK, (x + 60, y + 70, 30, 70))

    # Draw trees
    for (x, y) in trees:
        pygame.draw.rect(screen, TREE_TRUNK, (x, y, 20, 100))  # Tree trunk
        pygame.draw.circle(screen, TREE_LEAF, (x + 10, y - 20), 30)  # Tree leaf

    # Draw the falling leaves
    for leaf in leaves:
        pygame.draw.circle(screen, leaf[2], (leaf[0], leaf[1]), 4)

    # Draw sun or moon
    if is_day:
        pygame.draw.circle(screen, (255, 255, 0), sun_position, 30)  # Sun
        pygame.draw.rect(screen, CAR_COLOR_DAY, (car_position_day[0], car_position_day[1], 60, 30))  # Day car
        pygame.draw.circle(screen, (0, 0, 0), (car_position_day[0] + 10, car_position_day[1] + 30), 10)  # Left wheel
        pygame.draw.circle(screen, (0, 0, 0), (car_position_day[0] + 50, car_position_day[1] + 30), 10)  # Right wheel
    else:
        pygame.draw.circle(screen, (200, 200, 200), moon_position, 25)  # Moon
        for star in stars:
            pygame.draw.circle(screen, STAR_COLOR, star, 2)  # Stars at night
        pygame.draw.rect(screen, CAR_COLOR_NIGHT, (car_position_night[0], car_position_night[1], 60, 30))  # Night car
        pygame.draw.circle(screen, (0, 0, 0), (car_position_night[0] + 10, car_position_night[1] + 30), 10)  # Left wheel
        pygame.draw.circle(screen, (0, 0, 0), (car_position_night[0] + 50, car_position_night[1] + 30), 10)  # Right wheel

    # Draw road
    pygame.draw.rect(screen, ROAD_COLOR, (0, HEIGHT - 40, WIDTH, 40))
    for i in range(0, WIDTH, 100):  # Road lines
        pygame.draw.rect(screen, ROAD_LINE_COLOR, (i, HEIGHT - 20, 50, 5))

    # Display update
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()