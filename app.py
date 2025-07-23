import pygame
import random
import sys

pygame.init()

# Global settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 800
SNAKE_WIDTH, SNAKE_HEIGHT = 1200, 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Classic Games')
clock = pygame.time.Clock()

CELL_SIZE=20
# Fonts
font_small = pygame.font.SysFont('Arial', 24)
font_medium = pygame.font.SysFont('Arial', 36)
font_large = pygame.font.SysFont('Arial', 60)

# Global colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
GRAY = (180, 180, 180)
ROAD_COLOR = (20, 20, 20)
LINE_COLOR = (200, 200, 0)

# Car dimensions
CAR_WIDTH, CAR_HEIGHT = 60, 120

# Load car images
try:
    player_car_img = pygame.image.load("player_car.png")
    enemy_car_img = pygame.image.load("enemy_car.png")
    player_car_img = pygame.transform.scale(player_car_img, (CAR_WIDTH, CAR_HEIGHT))
    enemy_car_img = pygame.transform.scale(enemy_car_img, (CAR_WIDTH, CAR_HEIGHT))
except:
    print("Make sure player_car.png and enemy_car.jpg are present.")
    pygame.quit()
    sys.exit()

# Main menu
def main_menu():
    while True:
        screen.fill(BLACK)
        title = font_large.render("Select a Game", True, GREEN)
        option1 = font_medium.render("1. Snake Game", True, WHITE)
        option2 = font_medium.render("2. Lane Car Racing", True, WHITE)
        option_quit = font_medium.render("Q. Quit", True, RED)

        screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 200))
        screen.blit(option1, (WINDOW_WIDTH//2 - option1.get_width()//2, 300))
        screen.blit(option2, (WINDOW_WIDTH//2 - option2.get_width()//2, 370))
        screen.blit(option_quit, (WINDOW_WIDTH//2 - option_quit.get_width()//2, 440))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_game()
                elif event.key == pygame.K_2:
                    car_racing_game()
                elif event.key == pygame.K_q:
                    pygame.quit(); sys.exit()

# Helper for text
def draw_text(text, x, y, color=WHITE, center=True, size=36):
    font = pygame.font.SysFont('Arial', size)
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(x, y) if center else (x, y))
    screen.blit(txt, rect)

def get_random_food_position(snake_positions):
    while True:
        pos = [
            random.randrange(0, WINDOW_WIDTH// CELL_SIZE) * CELL_SIZE,
            random.randrange(0, WINDOW_HEIGHT // CELL_SIZE) * CELL_SIZE
        ]
        if pos not in snake_positions:
            return pos
# Snake Game
def snake_game():
    SPEED = snake_menu()
    snake_pos = [[100, 100], [80, 100], [60, 100]]
    snake_dir = 'RIGHT'
    move_x, move_y = CELL_SIZE, 0
    direction_changed = False
    food_pos = get_random_food_position(snake_pos)
    score = 0
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not direction_changed:
                    if event.key == pygame.K_UP and snake_dir != 'DOWN':
                        snake_dir = 'UP'
                        move_x, move_y = 0, -CELL_SIZE
                        direction_changed = True
                    elif event.key == pygame.K_DOWN and snake_dir != 'UP':
                        snake_dir = 'DOWN'
                        move_x, move_y = 0, CELL_SIZE
                        direction_changed = True
                    elif event.key == pygame.K_LEFT and snake_dir != 'RIGHT':
                        snake_dir = 'LEFT'
                        move_x, move_y = -CELL_SIZE, 0
                        direction_changed = True
                    elif event.key == pygame.K_RIGHT and snake_dir != 'LEFT':
                        snake_dir = 'RIGHT'
                        move_x, move_y = CELL_SIZE, 0
                        direction_changed = True
                if event.key == pygame.K_q:
                    pygame.quit(); sys.exit()

        # Move snake
        new_head = [snake_pos[0][0] + move_x, snake_pos[0][1] + move_y]
        snake_pos.insert(0, new_head)

        # --- Food Collision Check ---
        if snake_pos[0][0] == food_pos[0] and snake_pos[0][1] == food_pos[1]:
            score += 1
            food_pos = get_random_food_position(snake_pos)
        else:
            snake_pos.pop()

        # --- Draw Snake ---
        for i, pos in enumerate(snake_pos):
            color = GREEN if i == 0 else (0, max(150, 255 - i*10), 0)
            pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE), 1)

        # --- Draw Food (Red Circle + Highlight + Leaf) ---
        food_center = (food_pos[0] + CELL_SIZE // 2, food_pos[1] + CELL_SIZE // 2)
        pygame.draw.circle(screen, RED, food_center, CELL_SIZE // 2)
        pygame.draw.circle(screen, (255, 200, 200), (food_center[0], food_pos[1] + CELL_SIZE // 3), CELL_SIZE // 5)
        leaf_points = [
            (food_center[0], food_pos[1]),  # Top center
            (food_center[0] + CELL_SIZE // 4, food_pos[1] + CELL_SIZE // 4),  # Right
            (food_center[0], food_pos[1] + CELL_SIZE // 2),  # Bottom
            (food_center[0] - CELL_SIZE // 4, food_pos[1] + CELL_SIZE // 4)  # Left
        ]
        pygame.draw.polygon(screen, (0, 255, 0), leaf_points)

        # --- Wall or Self Collision? ---
        if (
            snake_pos[0][0] < 0 or snake_pos[0][0] >= SNAKE_WIDTH or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= SNAKE_HEIGHT or
            snake_pos[0] in snake_pos[1:]
        ):
            draw_text("Game Over - Press R to Restart or Q to Quit", SNAKE_WIDTH//2, SNAKE_HEIGHT//2,RED, size=32)
            pygame.display.flip()
            pygame.time.wait(800)
            # Wait for restart or quit
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit(); sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            snake_game(); return
                        if event.key == pygame.K_q:
                            pygame.quit(); sys.exit()

        draw_text(f"Score: {score}", 70, 30, WHITE, center=False, size=24)
        pygame.display.flip()
        clock.tick(SPEED)
        direction_changed = False
# Menu to select difficulty
def snake_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Select Snake Difficulty", WINDOW_WIDTH//2, 200, GREEN)
        draw_text("1. Easy", WINDOW_WIDTH//2, 280)
        draw_text("2. Medium", WINDOW_WIDTH//2, 340)
        draw_text("3. Hard", WINDOW_WIDTH//2, 400)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 8
                elif event.key == pygame.K_2:
                    return 15
                elif event.key == pygame.K_3:
                    return 25

# Lane Car Racing Game
def car_racing_game():
    LANE_COUNT = 6
    LANE_WIDTH = WINDOW_WIDTH // (LANE_COUNT + 1)
    LANE_X = [LANE_WIDTH * (i + 1) - 30 for i in range(LANE_COUNT)]
    BUTTON_W, BUTTON_H = 80, 60
    y = WINDOW_HEIGHT - CAR_HEIGHT - 20
    player_lane = LANE_COUNT // 2
    score = 0
    enemy_speed = car_menu()
    game_over = False
    move_cooldown = 0
    min_y = 40
    max_y = WINDOW_HEIGHT - CAR_HEIGHT - 20
    step_y = 40
    FPS = 60

    enemy_list = [{"lane": random.randint(0, LANE_COUNT - 1), "y": random.randint(-600, -CAR_HEIGHT)}]
    enemy_threshold = 10
    max_enemy_count = 8

    while True:
        screen.fill((20, 120, 20))
        pygame.draw.rect(screen, ROAD_COLOR, (LANE_WIDTH // 2, 0, WINDOW_WIDTH - LANE_WIDTH, WINDOW_HEIGHT))
        for i in range(1, LANE_COUNT):
            x = LANE_WIDTH * (i + 0.5)
            for yy in range(0, WINDOW_HEIGHT, 40):
                pygame.draw.rect(screen, LINE_COLOR, (x - 3, yy, 6, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    car_racing_game()
                    return
                elif event.key == pygame.K_q:
                    return

        keys = pygame.key.get_pressed()
        if move_cooldown == 0 and not game_over:
            if keys[pygame.K_LEFT] and player_lane > 0:
                player_lane -= 1
                move_cooldown = 8
            if keys[pygame.K_RIGHT] and player_lane < LANE_COUNT - 1:
                player_lane += 1
                move_cooldown = 8
            if keys[pygame.K_UP] and y > min_y:
                y -= step_y
                move_cooldown = 8
            if keys[pygame.K_DOWN] and y < max_y:
                y += step_y
                move_cooldown = 8
        else:
            move_cooldown = max(move_cooldown - 1, 0)

        if not game_over:
            if score >= enemy_threshold and len(enemy_list) < max_enemy_count:
                enemy_list.append({"lane": random.randint(0, LANE_COUNT - 1), "y": random.randint(-600, -CAR_HEIGHT)})
                enemy_threshold += 5

            px = LANE_X[player_lane]
            screen.blit(player_car_img, (px, y))
            player_rect = pygame.Rect(px, y, CAR_WIDTH, CAR_HEIGHT)

            for enemy in enemy_list:
                enemy["y"] += enemy_speed
                ex = LANE_X[enemy["lane"]]
                screen.blit(enemy_car_img, (ex, enemy["y"]))
                enemy_rect = pygame.Rect(ex, enemy["y"], CAR_WIDTH, CAR_HEIGHT)
                if player_rect.colliderect(enemy_rect):
                    game_over = True
                if enemy["y"] > WINDOW_HEIGHT:
                    enemy["lane"] = random.randint(0, LANE_COUNT - 1)
                    enemy["y"] = random.randint(-600, -CAR_HEIGHT)
                    score += 1
                    if score % 5 == 0:
                        enemy_speed += 1

            draw_text(f"Score: {score}", WINDOW_WIDTH // 2, 40, WHITE, size=30)
        else:
            draw_text("GAME OVER!", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60, RED, size=64)
            draw_text(f"Final Score: {score}", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, WHITE)
            draw_text("Press R to Restart or Q to Menu", WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60, WHITE, size=24)

        pygame.display.flip()
        clock.tick(FPS)

# Menu to select difficulty
def car_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Select Race Difficulty", WINDOW_WIDTH//2, 200, GREEN)
        draw_text("1. Easy", WINDOW_WIDTH//2, 280)
        draw_text("2. Medium", WINDOW_WIDTH//2, 340)
        draw_text("3. Hard", WINDOW_WIDTH//2, 400)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 10
                elif event.key == pygame.K_2:
                    return 15
                elif event.key == pygame.K_3:
                    return 20


# Run the game
if __name__ == '__main__':
    main_menu()
