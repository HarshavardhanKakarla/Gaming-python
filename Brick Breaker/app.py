import pygame, sys, random

# === Constants ===
WIDTH, HEIGHT = 800, 600
FPS = 60
PADDLE_W, PADDLE_H = 100, 15
BALL_RADIUS = 10
BRICK_ROWS, BRICK_COLS = 6, 10
BRICK_W = WIDTH // BRICK_COLS
BRICK_H = 20

# === Colors ===
WHITE, BLACK = (255,255,255), (0,0,0)
RED, GREEN, BLUE = (255,0,0), (0,255,0), (0,0,255)
GRAY = (100, 100, 100)
YELLOW, CYAN, MAGENTA = (255,255,0), (0,255,255), (255,0,255)
BRICK = (142,71,56) 


# === Game Classes ===
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_W, PADDLE_H))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(midbottom=(WIDTH//2, HEIGHT - 30))
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH: self.rect.x += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.dx = speed * random.choice([-1, 1])
        self.dy = -speed
        self.base_speed = speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left <= 0 or self.rect.right >= WIDTH: self.dx *= -1
        if self.rect.top <= 0: self.dy *= -1

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BRICK_W, BRICK_H))
        self.image.fill(color)
        pygame.draw.rect(self.image, GRAY, self.image.get_rect(), 2)
        self.rect = self.image.get_rect(topleft=(x, y))

# === Utility ===
def draw_text(screen, text, x, y, font, color=WHITE, center=True):
    label = font.render(text, True, color)
    pos = (x - label.get_width()//2, y) if center else (x, y)
    screen.blit(label, pos)

def generate_bricks():
    bricks = pygame.sprite.Group()
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = col * BRICK_W
            y = row * BRICK_H + 50
           
            bricks.add(Brick(x, y, BRICK))
    return bricks

# === Menus ===
def main_menu(screen, font):
    while True:
        screen.fill(BLACK)
        draw_text(screen, "Brick Breaker", WIDTH//2, HEIGHT//2 - 60, font, color=CYAN)
        draw_text(screen, "S = Start | Q = Quit", WIDTH//2, HEIGHT//2, font, color=YELLOW)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: return True
                if event.key == pygame.K_q: pygame.quit(); sys.exit()

def difficulty_menu(screen, font):
    options = ["Easy", "Medium", "Hard"]
    speeds = [3, 5, 7]
    selected = 1
    while True:
        screen.fill(BLACK)
        draw_text(screen, "Select Difficulty:", WIDTH//2, HEIGHT//2 - 80, font, color=CYAN)
        for i, label in enumerate(options):
            prefix = ">" if i == selected else " "
            draw_text(screen, f"{prefix} {label}", WIDTH//2, HEIGHT//2 - 20 + i*40, font, color=WHITE)
        draw_text(screen, "ENTER = Confirm | Q = Quit", WIDTH//2, HEIGHT - 40, font, color=YELLOW)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: selected = max(0, selected - 1)
                if event.key == pygame.K_DOWN: selected = min(2, selected + 1)
                if event.key == pygame.K_q: pygame.quit(); sys.exit()
                if event.key == pygame.K_RETURN: return speeds[selected]
# === Gameplay ===
def run_game(screen, font, ball_speed):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    paddle = Paddle()
    ball = Ball(ball_speed)
    bricks = generate_bricks()
    all_sprites.add(paddle, ball)
    all_sprites.add(bricks)
    paddle_group = pygame.sprite.GroupSingle(paddle)
    score = 0
    running = True
    paused = False

    while running:
        clock.tick(FPS)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_q: return
                if ev.key == pygame.K_SPACE: paused = not paused
        if not paused:     
            all_sprites.update()

        if pygame.sprite.spritecollide(ball, paddle_group, False):
            ball.dy *= -1
            offset = (ball.rect.centerx - paddle.rect.centerx) / (PADDLE_W / 2)
            ball.dx = ball.base_speed * offset

        hits = pygame.sprite.spritecollide(ball, bricks, True)
        if hits:
            ball.dy *= -1
            score += len(hits) * 10

        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text(screen, f"Score: {score}", 10, 10, font, color=GREEN, center=False)

        if paused:
            draw_text(screen, "PAUSED", WIDTH//2, HEIGHT//2, font, color=YELLOW)


        if ball.rect.top > HEIGHT:
            draw_text(screen, "Game Over", WIDTH//2, HEIGHT//2, font, color=MAGENTA)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        if not bricks:
            draw_text(screen, "You Win!", WIDTH//2, HEIGHT//2, font, color=MAGENTA)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        pygame.display.flip()

# === Entry Point ===
def main():
    pygame.init()
    pygame.mixer.init()
  # Replace the music file with your file in the below line
    pygame.mixer.music.load("assets/bgm.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brick Breaker")
    font = pygame.font.SysFont("Arial", 28)

    while True:
        if main_menu(screen, font):
            ball_speed = difficulty_menu(screen, font)
            run_game(screen, font, ball_speed)

if __name__ == "__main__":
    main()
