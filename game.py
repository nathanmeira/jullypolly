import pygame
import random
from pygame.locals import *

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("JullyPolly")
clock = pygame.time.Clock()
white = (255,255,255)

jullyImg = pygame.image.load('personagem/imagens/jully2.png')
carrotImg = pygame.image.load('personagem/imagens/carrot.png')
strawberryImg = pygame.image.load('personagem/imagens/strawberry.png')
grapeImg = pygame.image.load('personagem/imagens/grape.png')
hotdogImg = pygame.image.load('personagem/imagens/doggy.png')
frisbeeImg = pygame.image.load('personagem/imagens/frisbee.png')

food1 = [carrotImg,strawberryImg,grapeImg,hotdogImg]

class Main:
    def __init__(self, x,y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.food_img = None
        self.projectile = None
        self.projectile = []
        self.cool_down = 0
    
    def draw(self,window):
        window.blit(self.food_img, (self.x, self.y))

    def get_width(self):
        return self.food_img.get_width()
    
    def get_height(self):
        return self.food_img.get_height()

class Player(Main):
    def __init__(self, x,y, health=100):
        super().__init__(x,y,health)
        self.food_img = jullyImg
        self.projectile = frisbeeImg
        self.mask = pygame.mask.from_surface(self.food_img)
        self.max_health = health

class Food(Main):
    FOOD_MAP = {
        "carrot": carrotImg,
        "strawberry": strawberryImg,
        "grape": grapeImg,
        "hotdog": hotdogImg
    }

    def __init__(self,x,y,type):
        super().__init__(x,y)
        self.food_img = self.FOOD_MAP[type]
        self.mask = pygame.mask.from_surface(self.food_img)

    def move(self,vel):
        self.y += vel

def food(x,y):
    food_rand = random.choice(food1) 
    screen.blit(food_rand,(x,y))

def game_loop():
    run = True
    FPS = 60
    level = 0
    lives = 3
    main_font = pygame.font.SysFont("comicsans",50)
    foods = []
    wave_length = 5
    food_vel = 1.5
    player_vel = 7
    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.78)
 
    player = Player(x,y)

    def draw():
        lives_label = main_font.render(f"Lives: {lives}",1,(0,0,0))
        level_label = main_font.render(f"Level: {level}",1,(0,0,0))
        screen.blit(lives_label,(10,10))
        screen.blit(level_label,(WIDTH - level_label.get_width() - 10,10))

        for food in foods:
            food.draw(screen)
            
        player.draw(screen)

    while run:
        clock.tick(FPS)

        if len(foods) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                food = Food(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["carrot", "strawberry", "grape", "hotdog"]))
                foods.append(food)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:
            player.x -= player_vel 
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel

        for food in foods[:]:
            food.move(food_vel)
            if food.y + food.get_height() > HEIGHT:
                foods.remove(food)

        screen.fill(white)
        draw()
        pygame.display.update()
        
game_loop()