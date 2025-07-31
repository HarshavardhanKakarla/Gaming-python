import random, sys, pygame

# ───────────────────────────────────────────────
SCREEN_W, SCREEN_H = 800, 600
FPS = 60
BG_COLOR = (25, 30, 40)
TITLE_BG_COLOR = (10, 10, 10)
TILE_COLOR = (70, 140, 220)
INPUT_BOX_COLOR_ACTIVE = (250, 220, 70)
INPUT_BOX_COLOR_INACTIVE = (150, 150, 150)
TILE_SIZE = 64
GAP = 10
FONT_NAME = pygame.font.get_default_font()

# Time limits for each difficulty (in seconds)
TIME_LIMITS = {
    'easy': 45,
    'medium': 30,
    'hard': 15,
}

# Preloaded word list (length 6-10 letters)
WORDS = [
    "ability", "absence", "academy", "account", "accused", "achieve", "acquire", "address", "advance",
    "adverse", "advised", "adviser", "against", "airline", "airport", "alcohol", "alleged", "already",
    "analyst", "ancient", "anxiety", "anxious", "anybody", "applied", "arrived", "assault", "attempt",
    "attract", "auction", "average", "backing", "balance", "banking", "barrier", "battery", "because",
    "bedroom", "believe", "beneath", "benefit", "besides", "between", "billion", "binding", "brother",
    "brought", "burning", "cabinet", "caliber", "calling", "capable", "capital", "captain", "caption",
    "capture", "careful", "carrier", "caution", "ceiling", "central", "century", "certain", "chamber",
    "channel", "chapter", "charity", "charlie", "charter", "checked", "chicken", "chronic", "circuit",
    "classes", "classic", "climate", "closing", "closure", "clothes", "collect", "college", "combine",
    "comfort", "command", "comment", "compact", "company", "compare", "compete", "complex", "concept",
    "concern", "concert", "conduct", "confirm", "connect", "consent", "consist", "contact", "contain",
    "content", "contest", "context", "control", "convert", "cooking", "cooling", "correct", "cottage",
    "cotton", "council", "counsel", "counter", "country", "crucial", "crystal", "culture", "current",
    "cutting", "decent", "decided", "decline", "default", "defence", "deficit", "deliver", "density",
    "deposit", "desktop", "despite", "destroy", "device", "devote", "digital", "dilemma", "dining",
    "dinner", "direct", "district", "diverse", "divided", "drawing", "driving", "dynamic", "eastern",
    "economy", "edition", "elderly", "element", "engaged", "enhance", "essence", "evening", "evident",
    "exactly", "examine", "example", "excited", "exclude", "execute", "exercise", "exhibit", "expense",
    "explain", "explore", "express", "extreme", "factory", "faculty", "failing", "failure", "feature",
    "federal", "feeling", "fiction", "fifteen", "filling", "finance", "finding", "fishing", "fitness",
    "foreign", "formula", "fortune", "forward", "founder", "freedom", "further", "gallery", "general",
    "genetic", "genuine", "gesture", "greater", "hanging", "heading", "healthy", "hearing", "heavily",
    "helpful", "helping", "herself", "highway", "himself", "history", "holding", "holiday", "housing",
    "however", "hundred", "husband", "illegal", "illness", "imagine", "imaging", "improve", "include",
    "initial", "inquiry", "insight", "install", "instead", "intense", "interim", "involve", "jointly",
    "journal", "journey", "justice", "justify", "kitchen", "knowing", "landing", "largest", "lasting",
    "learning", "leaving", "lecture", "library", "license", "limited", "listing", "logical", "loyalty",
    "machine", "manager", "married", "massive", "meaning", "measure", "medical", "meeting", "mention",
    "message", "million", "mineral", "minimal", "minimum", "missing", "mission", "mistake", "mixture",
    "monitor", "monthly", "morning", "musical", "mystery", "natural", "needing", "nervous", "network",
    "nothing", "nowhere", "nuclear", "offense", "officer", "ongoing", "opening", "operate", "opinions",
    "organic", "outcome", "outdoor", "outlook", "outside", "overall", "package", "painting", "parking",
    "partial", "partner", "passage", "passing", "passion", "passive", "pattern", "payable", "payment",
    "payroll", "penalty", "pension", "percent", "perfect", "perform", "perhaps", "phoenix", "picking",
    "picnic", "pioneer", "plastic", "pointed", "popular", "portion", "poverty", "precise", "predict",
    "premier", "premium", "prepare", "present", "prevent", "primary", "printer", "privacy", "private",
    "problem", "proceed", "process", "produce", "product", "profile", "program", "project", "promise",
    "promote", "protect", "protein", "protest", "provide", "publish", "purpose", "pursuit", "qualify",
    "quality", "quarter", "radical", "random", "rapidly", "reading", "reality", "realize", "receipt",
    "receive", "recover", "reflect", "reform", "refugee", "refusal", "regard", "regimen", "region",
    "regular", "related", "release", "relevant", "reliable", "relieve", "remains", "removal", "removed",
    "replace", "request", "require", "reserve", "resolve", "respect", "respond", "restore", "retired",
    "revenue", "reverse", "rolling", "routine", "running", "satisfy", "saving", "saying", "science",
    "section", "segment", "serious", "servant", "serving", "session", "setting", "seventh", "severe",
    "sharing", "shortly", "showing", "sickly", "silence", "similar", "sitting", "sixteen", "skilled",
    "smoking", "sodium", "softly", "solely", "somehow", "someone", "speaker", "special", "species",
    "sponsor", "station", "storage", "strange", "stretch", "student", "studied", "subject", "suggest",
    "summary", "support", "suppose", "supreme", "surface", "surgery", "surplus", "survive", "suspect",
    "sustain", "teacher", "teaming", "telling", "tension", "therapy", "thereby", "thought", "through",
    "tonight", "totally", "towards", "traffic", "trouble", "turning", "typical", "unable", "unaware",
    "unclear", "uncover", "undergo", "unknown", "unusual", "upgrade", "utility", "variety", "various",
    "vehicle", "venture", "version", "victim", "violent", "virtual", "visible", "waiting", "walking",
    "wanting", "warning", "wedding", "weekend", "welcome", "welfare", "western", "whereas", "whether",
    "willing", "winning", "without", "witness", "writing", "written", "younger"
]

USED = set()

def new_word():
    global USED
    if len(USED) >= len(WORDS):
        USED.clear()

    remaining_words = [w for w in WORDS if w not in USED]

    if not remaining_words:
        USED.clear()
        remaining_words = WORDS[:]

    choice = random.choice(remaining_words)
    USED.add(choice)
    return choice

def tile_rects(word):
    total_w = len(word)*TILE_SIZE + (len(word)-1)*GAP
    x0 = (SCREEN_W - total_w)//2
    y = SCREEN_H//3
    return [pygame.Rect(x0 + i*(TILE_SIZE + GAP), y, TILE_SIZE, TILE_SIZE) for i in range(len(word))]

def draw_tiles(surface, letters, rects, font):
    for ch, r in zip(letters, rects):
        pygame.draw.rect(surface, TILE_COLOR, r, border_radius=8)
        txt = font.render(ch.upper(), True, (255, 255, 255))
        surface.blit(txt, txt.get_rect(center=r.center))

def center_text(surface, msg, font, dy=0, color=(240, 240, 240)):
    img = font.render(msg, True, color)
    rect = img.get_rect(center=(SCREEN_W//2, SCREEN_H//2 + dy))
    surface.blit(img, rect)

def draw_input_box(surface, rect, text, font, active):
    color = INPUT_BOX_COLOR_ACTIVE if active else INPUT_BOX_COLOR_INACTIVE
    pygame.draw.rect(surface, color, rect, border_radius=6)
    txt_surf = font.render(text, True, (255, 255, 255))
    padding = 6
    txt_rect = txt_surf.get_rect(midleft=(rect.x + padding, rect.centery))
    surface.blit(txt_surf, txt_rect)

def main():
    pygame.init()
    pygame.mixer.init()
    try:
      # Replace the music with your own file in the below line
        pygame.mixer.music.load("assets/bgm.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Music file not found, continuing without music.")

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Word Finder - Difficulty Select")
    clock = pygame.time.Clock()

    font_tile = pygame.font.Font(FONT_NAME, 50)
    font_big = pygame.font.Font(FONT_NAME, 60)
    font_ui = pygame.font.Font(FONT_NAME, 32)
    font_title = pygame.font.Font(FONT_NAME, 72)

    input_box_rect = pygame.Rect((SCREEN_W - 400)//1.8, SCREEN_H//3 + 120, 320, 80)

    STATE_TITLE = 0
    STATE_PLAYING = 1
    STATE_RESULT = 2
    state = STATE_TITLE

    difficulty = None
    time_limit = 0
    score=0

    word = ""
    letters = []
    rects = []
    user_in = ""
    start = 0
    finish = 0
    elapsed = 0
    input_active = True

    def start_game():
        nonlocal word, letters, rects, user_in, start, elapsed, input_active, state
        word = new_word()
        letters = random.sample(word, len(word))
        rects = tile_rects(word)
        user_in = ""
        start = pygame.time.get_ticks()
        elapsed = 0
        input_active = True
        state = STATE_PLAYING

    running = True
    while running:
        dt = clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    running = False

                if state == STATE_TITLE:
                    if e.key == pygame.K_1:
                        difficulty = 'easy'
                    elif e.key == pygame.K_2:
                        difficulty = 'medium'
                    elif e.key == pygame.K_3:
                        difficulty = 'hard'
                    if difficulty:
                        time_limit = TIME_LIMITS[difficulty]
                        pygame.display.set_caption(f"Word Finder - {difficulty.capitalize()} Mode")
                        score=0
                        start_game()

                elif state == STATE_PLAYING:
                    if input_active:
                        if e.key == pygame.K_BACKSPACE:
                            user_in = user_in[:-1]
                        elif e.key == pygame.K_RETURN:
                            if user_in.lower() == word:
                                finish = (pygame.time.get_ticks() - start) / 1000
                                input_active = False
                                state = STATE_RESULT
                                score += 1
                            else:
                                screen.fill((160, 50, 50))
                                pygame.display.flip()
                                pygame.time.delay(120)
                        elif e.unicode.isalpha():
                            if len(user_in) < len(word):
                                user_in += e.unicode.lower()

                elif state == STATE_RESULT:
                    # Any key press goes to next round
                    start_game()

        if state == STATE_PLAYING:
            elapsed = (pygame.time.get_ticks() - start) / 1000
            if time_limit and elapsed >= time_limit:
                state = STATE_RESULT
                finish = "TIME UP"
                input_active = False

        if state == STATE_TITLE:
            screen.fill(TITLE_BG_COLOR)
            center_text(screen, "WORD FINDER", font_title, dy=-130, color=(250, 220, 70))
            center_text(screen, "Select Difficulty:", font_ui, dy=-40, color=(240, 240, 240))
            center_text(screen, "1 - Easy (45's)", font_ui, dy=10, color=(120, 240, 120))
            center_text(screen, "2 - Medium (30's)", font_ui, dy=50, color=(240, 240, 120))
            center_text(screen, "3 - Hard (15's)", font_ui, dy=90, color=(240, 120, 120))
            center_text(screen, "Press Q to Quit", font_ui, dy=160, color=(180, 180, 180))
        else:
            screen.fill(BG_COLOR)
            draw_tiles(screen, letters, rects, font_tile)
            draw_input_box(screen, input_box_rect, user_in.upper(), font_big, input_active)
            tcol = (120, 240, 120) if state == STATE_PLAYING else (240, 240, 240)
            center_text(screen, f"{elapsed:0.1f}s / {time_limit}s", font_ui, dy=-220, color=tcol)

            score_text = font_ui.render(f"Score: {score}", True, (250,220,70))
            screen.blit(score_text, (20, 20))


            if state == STATE_RESULT:
                if finish == "TIME UP":
                    msg = f"Time's up! The word was {word.upper()}"
                else:
                    msg = f"Good job! {word.upper()} • {finish:0.2f}s"
                center_text(screen, msg, font_ui, dy=220)
                center_text(screen, "Press ANY KEY for new word", font_ui, dy=260, color=(180, 180, 180))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
