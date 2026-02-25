import pygame, pygame_menu, random, math, sys, os
from pygame.locals import *

DIFFICULTY = {
  "max_score_scale": 100,

  "spawn_decay": 0.97,
  "spawn_max_delay": 1000,
  "spawn_min_delay": 100,

  "enemy_speed_growth": 1.02,
  "enemy_speed_cap": 8,

  "player_speed_base": 3,
  "player_speed_growth": 1/20,
  "player_speed_cap": 6,

  "fire_upper_decay": 0.90,
  "fire_lower_decay": 0.95,
  "fire_upper_max": 5000,
  "fire_lower_max": 1000,
  "fire_upper_min": 600,
  "fire_lower_min": 300,
}

def resource_path(relative_path):
  try:
    base_path = sys._MEIPASS
  except Exception:
    base_path = os.path.abspath(".")
  return os.path.join(base_path, relative_path)

def mainmenu():
  pygame.init()
  pygame.mixer.init()
  surface = pygame.display.set_mode((640, 480))
  pygame.display.set_caption("War Plane")

  def start_the_game():
    pygame.mixer.music.stop()
    main(surface)

  mytheme = pygame_menu.Theme(
    background_color=pygame_menu.baseimage.BaseImage(image_path=resource_path("backgrounds/camo.png"), drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY),
    title_background_color=(0, 0, 0),
    widget_padding=25,
    title_font=resource_path("fonts/Farenheight.ttf"),
    widget_font=resource_path("fonts/Farenheight.ttf"),
    widget_background_color=(0, 0, 0),
    title_font_size=64,
    title_offset=(0, 7.5),
    title_font_antialias=True,
    widget_font_antialias=True,
    widget_margin=(0, 10),
    widget_font_size=32,
  )

  menu = pygame_menu.Menu('War Plane', 640, 480, theme=mytheme)
  menu.add.button('Play', start_the_game)
  menu.add.button('Quit', pygame_menu.events.EXIT, selection_color=(150, 10, 0))

  pygame.mixer.music.load(resource_path("sfx/war-is-coming.mp3"))
  pygame.mixer.music.play(-1)
  
  menu.mainloop(surface)

def main(screen):
  screenWidth = 640
  screenHeight = 480
  clock = pygame.time.Clock()

  player = None
  enemies = None
  bullets = None
  enemybullets = None
  all_sprites = None
  ammo = 10
  score = 0
  scroll = 0.0
  end = False
  game_over_cleaned = False

  player_img = pygame.transform.smoothscale(pygame.image.load(resource_path('sprites/playerplane.png')).convert_alpha(), (64, 64))
  enemy_img = pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load(resource_path('sprites/enemyplane.png')).convert_alpha(), (64, 64)), False, True)
  bullet_img = pygame.transform.smoothscale(pygame.image.load(resource_path('sprites/bullet.png')).convert_alpha(), (16, 16))
  enemy_bullet_img = pygame.transform.smoothscale(pygame.image.load(resource_path('sprites/enemybullet.png')).convert_alpha(), (16, 16))

  def reset_game():
    nonlocal player, enemies, bullets, enemybullets, all_sprites, ammo, score, end, scroll, game_over_cleaned

    ammo = 10
    score = 0
    scroll = 0.0
    end = False
    game_over_cleaned = False

    player = Player()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemybullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    update_spawn_timer()

    pygame.mixer.music.load(resource_path("sfx/propeller.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

  def get_difficulty_scales():
    difficulty = min(score, DIFFICULTY["max_score_scale"])
    return {
        "spawn": DIFFICULTY["spawn_decay"] ** difficulty,
        "speed": DIFFICULTY["enemy_speed_growth"] ** difficulty,
        "fire_upper": DIFFICULTY["fire_upper_decay"] ** difficulty,
        "fire_lower": DIFFICULTY["fire_lower_decay"] ** difficulty,
    }

  def update_spawn_timer():
    scales = get_difficulty_scales()
    delay = max(DIFFICULTY["spawn_min_delay"], int(DIFFICULTY["spawn_max_delay"] * scales["spawn"]))
    pygame.time.set_timer(ADDENEMY, delay)

  class Player(pygame.sprite.Sprite):
    def __init__(self):
      super(Player, self).__init__()
      self.surf = player_img
      self.mask = pygame.mask.from_surface(self.surf)
      self.rect = self.surf.get_rect()
      self.rect.x = (screenWidth - self.rect.width) // 2
      self.rect.y = screenHeight - 2 * self.rect.height
      self.pos_x = float(self.rect.x)
      self.pos_y = float(self.rect.y)
      self.speed = 3

    def update(self):
      self.speed = min(DIFFICULTY["player_speed_cap"], DIFFICULTY["player_speed_base"] + score * DIFFICULTY["player_speed_growth"])

      keys = pygame.key.get_pressed()
      if keys[K_UP] or keys[K_w]:
        self.pos_y -= self.speed
      if keys[K_DOWN] or keys[K_s]:
        self.pos_y += self.speed
      if keys[K_LEFT] or keys[K_a]:
        self.pos_x -= self.speed
      if keys[K_RIGHT] or keys[K_d]:
        self.pos_x += self.speed

      self.rect.x = int(self.pos_x)
      self.rect.y = int(self.pos_y)

      if self.rect.left < 0:
        self.rect.left = 0
        self.pos_x = self.rect.x
      if self.rect.bottom > screenHeight:
        self.rect.bottom = screenHeight
        self.pos_y = self.rect.y
      if self.rect.top < 0:
        self.rect.top = 0
        self.pos_y = self.rect.y
      if self.rect.right > screenWidth:
        self.rect.right = screenWidth
        self.pos_x = self.rect.x

  class Enemy(pygame.sprite.Sprite):
    width = 64
    height = 64
    initial_speed = 2

    def __init__(self):
      super(Enemy, self).__init__()
      self.surf = enemy_img
      self.mask = pygame.mask.from_surface(self.surf)
      self.x = random.randint(self.width // 2, screenWidth - self.width // 2)
      self.y = random.randint(-screenHeight, 0)
      self.rect = self.surf.get_rect(center=(self.x, self.y))
      self.pos_y = float(self.rect.y)
      self.speed = self.initial_speed
      self.fire_delay = random.randint(500, 5000)
      self.last_shot = pygame.time.get_ticks()

    def update(self, scales):
      self.speed = min(DIFFICULTY["enemy_speed_cap"], self.initial_speed * scales["speed"])
      self.pos_y += self.speed
      self.rect.y = int(self.pos_y)
      if self.rect.top > screenHeight:
        self.kill()

  class Bullet(pygame.sprite.Sprite):
    def __init__(self):
      super(Bullet, self).__init__()
      self.speed = -5
      self.surf = bullet_img
      self.mask = pygame.mask.from_surface(self.surf)
      self.rect = self.surf.get_rect()
      self.rect.centerx = player.rect.centerx
      self.rect.y = player.rect.top
      self.pos_y = float(self.rect.y)

    def update(self):
      self.pos_y += self.speed
      self.rect.y = int(self.pos_y)
      if self.rect.bottom < 0:
        self.kill()

  class EnemyBullet(Bullet):
    def __init__(self, enemy):
      super(EnemyBullet, self).__init__()
      self.speed = 2
      self.surf = enemy_bullet_img
      self.mask = pygame.mask.from_surface(self.surf)
      self.rect = self.surf.get_rect()
      self.rect.centerx = enemy.rect.centerx
      self.rect.y = enemy.rect.bottom
      self.pos_y = float(self.rect.y)

    def update(self):
      self.pos_y += self.speed
      self.rect.y = int(self.pos_y)
      if self.rect.top > screenHeight:
        self.kill()

  ADDENEMY = pygame.USEREVENT + 1

  bg = pygame.transform.smoothscale(pygame.image.load(resource_path("backgrounds/sand.png")).convert_alpha(), (screenWidth, screenHeight))
  tiles = math.ceil(screenHeight / bg.get_height()) + 1

  defaultfont = resource_path("fonts/AmericanCaptain.otf")
  font = pygame.font.Font(defaultfont, 32)
  gameoverFont = pygame.font.Font(defaultfont, 64)
  scoreFont = pygame.font.Font(defaultfont, 48)
  restartFont = pygame.font.Font(defaultfont, 32)

  gunfire = pygame.mixer.Sound(resource_path("sfx/gunfire.mp3"))

  reset_game()
  while True:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    scales = get_difficulty_scales()

    if not end:
      i = 0
      while (i < tiles):
        screen.blit(bg, (0, -(bg.get_height() * i + scroll)))
        i += 1
      scroll -= min(4, 1 + score * 0.02)
      if abs(scroll) > bg.get_height():
        scroll = 0.0

      for enemy in enemies:
        if current_time - enemy.last_shot > enemy.fire_delay:
          enemybullet = EnemyBullet(enemy)
          enemybullet.speed = 2 + enemy.speed
          enemybullets.add(enemybullet)
          all_sprites.add(enemybullet)
          enemy.last_shot = current_time

          upper = int(DIFFICULTY["fire_upper_max"] * scales["fire_upper"])
          lower = int(DIFFICULTY["fire_lower_max"] * scales["fire_lower"])
          upper = max(DIFFICULTY["fire_upper_min"], upper)
          lower = max(DIFFICULTY["fire_lower_min"], lower)
          enemy.fire_delay = random.randint(lower, max(lower + 1, upper))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if end:
        if event.type == pygame.KEYDOWN and event.key == K_RETURN:
          reset_game()

      if not end:
        if event.type == ADDENEMY:
          enemy = Enemy()
          enemy.initial_speed = random.uniform(2, 4)
          enemies.add(enemy)
          all_sprites.add(enemy)

        if event.type == pygame.KEYDOWN:
          if event.key == K_SPACE and ammo > 0:
            ammo -= 1
            pygame.mixer.Sound.play(gunfire)
            new_bullet = Bullet()
            bullets.add(new_bullet)
            all_sprites.add(new_bullet)

    if not end:
      player.update()
      enemies.update(scales)
      bullets.update()
      enemybullets.update()

      for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

      hit_enemy = pygame.sprite.spritecollideany(player, enemies, pygame.sprite.collide_mask)
      if hit_enemy:
        end = True

      if pygame.sprite.groupcollide(bullets, enemies, True, True, pygame.sprite.collide_mask):
        ammo = min(ammo + 2, 10)
        update_spawn_timer()
        score += 1

      hit_bullet = pygame.sprite.spritecollideany(player, enemybullets, pygame.sprite.collide_mask)
      if hit_bullet:
        end = True

      pygame.sprite.groupcollide(bullets, enemybullets, True, True, pygame.sprite.collide_mask)

      score_surface = font.render(f"Score: {score}", True, (0,0,0))
      screen.blit(score_surface, (4, 4))

      ammo_display = max(ammo, 0)
      ammo_surface = font.render(f"Ammo: {ammo_display}", True, (0,0,0))
      screen.blit(ammo_surface, (4, 36))

      if (ammo == 0 and len(bullets) == 0):
        end = True

    if end and not game_over_cleaned:
      pygame.mixer.music.stop()
      pygame.time.set_timer(ADDENEMY, 0)
      for entity in all_sprites:
        entity.kill()
      game_over_cleaned = True

    if end and game_over_cleaned:
      screen.blit(bg, (0, 0))
      gameover = gameoverFont.render("Game Over", 1, (255, 0, 0))
      endscore = scoreFont.render("Score: " + str(score), 1, (255, 0, 0))
      restart = restartFont.render("Press Enter to Restart", 1, (255, 0, 0))
      screen.blit(gameover, (screenWidth / 4, screenHeight / 4))
      screen.blit(endscore, (screenWidth / 4, screenHeight / 2.5))
      screen.blit(restart, (screenWidth / 4, screenHeight / 1.5))

    pygame.display.update()

mainmenu()
