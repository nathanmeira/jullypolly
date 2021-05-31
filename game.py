import pygame
import random
from pygame.locals import *

pygame.init()
WIDTH = 750 
HEIGHT = 750 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("JullyPolly")
clock = pygame.time.Clock()
white = (255,255,255)

jullyImg = pygame.image.load('personagem/imagens/jullyV2.png')
carrotImg = pygame.image.load('personagem/imagens/carrot.png')
strawberryImg = pygame.image.load('personagem/imagens/strawberry.png')
grapeImg = pygame.image.load('personagem/imagens/grape.png')
hotdogImg = pygame.image.load('personagem/imagens/doggy.png')
frisbeeImg = pygame.image.load('personagem/imagens/frisbeeV2.png')
BG = pygame.transform.scale(pygame.image.load('personagem/imagens/background.png'), (WIDTH, HEIGHT)) 
SCORE = 0 

class Frisbee:
    def __init__(self, x, y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Main:
    COOLDOWN = 30

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.food_img = None
        self.frisbee_img = None
        self.frisbees = []
        self.cool_down = 0
    
    def draw(self,window):
        window.blit(self.food_img, (self.x, self.y))
        for frisbee in self.frisbees:
            frisbee.draw(window)

    def move_frisbee(self, vel, obj):
        self.cooldown()
        for frisbee in self.frisbees:
            frisbee.move(vel)
            if frisbee.off_screen(HEIGHT):
                self.frisbees.remove(frisbee)
            elif frisbee.collision(obj):
                self.frisbees.remove(frisbee)

    def get_width(self):
        return self.food_img.get_width()
    
    def get_height(self):
        return self.food_img.get_height()

    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def shoot(self):
        if self.cool_down == 0:
            frisbee = Frisbee(self.x, self.y, self.frisbee_img)
            self.frisbees.append(frisbee)
            self.cool_down = 1

class Player(Main):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.food_img = jullyImg
        self.frisbee_img = frisbeeImg
        self.mask = pygame.mask.from_surface(self.food_img)
        self.max_health = health

    def move_frisbee(self, vel, objs):
        self.cooldown()
        for frisbee in self.frisbees:
            frisbee.move(vel)
            if frisbee.off_screen(HEIGHT):
                self.frisbees.remove(frisbee)
            else:
                for obj in objs:
                    if frisbee.collision(obj):
                        objs.remove(obj)
                        global SCORE
                        SCORE = SCORE + 1
                        if frisbee in self.frisbees:
                            self.frisbees.remove(frisbee)

    def collision(self, obj):
        return collide(self, obj)

class Food(Main):
    FOOD_MAP = {
        "carrot": carrotImg,
        "strawberry": strawberryImg,
        "grape": grapeImg,
        "hotdog": hotdogImg
    }

    def __init__(self,x,y,type):
        super().__init__(x,y,type)
        self.food_img = self.FOOD_MAP[type]
        self.mask = pygame.mask.from_surface(self.food_img)

    def move(self,vel):
        self.y += vel

def collide(obj1, obj2):
    offset_x = (int(obj2.x - obj1.x))
    offset_y = (int(obj2.y - obj1.y))
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def game_loop():
    global SCORE
    run = True
    FPS = 60
    level = 0
    lives = 3
    main_font = pygame.font.SysFont("comicsans",50)
    lost_font = pygame.font.SysFont("comicsans",60)
    enemy = []
    foods = []
    wave_length = 5
    enemy_vel = 1.5
    fruit_vel = 2
    vel_x = 10
    jump_y = 15
    jump = False
    frisbee_vel = 7
    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.78)
    lost = False
    lost_count = 0
     
    player = Player(x,y)

    def draw():
        screen.blit(BG, (0,0))
        lives_label = main_font.render(f"Vidas: {lives}",1,(0,0,0))
        level_label = main_font.render(f"Level: {level}",1,(0,0,0))
        score_label = main_font.render(f"Pontos: {SCORE}",1,(0,0,0))
        screen.blit(lives_label,(10,10))
        screen.blit(score_label,(10,60))
        screen.blit(level_label,(WIDTH - level_label.get_width() - 10,10))
        
        for hotdog in enemy:
            hotdog.draw(screen)
        for fruit in foods:
            fruit.draw(screen)

        player.draw(screen)

        if lost:
            lost_label = lost_font.render("Game Over!", 1, (0,0,0))
            screen.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 150))
        pygame.display.update()

    while run:
        clock.tick(FPS)  
        draw()
    
        if lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemy) == 0:
            level += 1
            wave_length += 2
            enemy_vel += 0.2
            for i in range(wave_length):
                hotdog = Food(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), "hotdog")
                fruit = Food(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["carrot", "strawberry", "grape"]))
                enemy.append(hotdog)
                foods.append(fruit) 
                   
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or keys[pygame.K_ESCAPE]:
                run = False
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - vel_x > 0:
            player.x -= vel_x 
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x + vel_x + player.get_width() < WIDTH:
            player.x += vel_x
        if keys[pygame.K_SPACE]:
            player.shoot()

        if jump is False and keys[pygame.K_w] or keys[pygame.K_UP]:
            jump = True
        
        if jump is True:
            player.y -= jump_y
            jump_y -= 1
            if jump_y < -15:
                jump = False
                jump_y = 15

        for hotdog in enemy[:]:
            hotdog.move(enemy_vel)
            if collide(hotdog, player):
                lives -= 1
                enemy.remove(hotdog)
            elif hotdog.y + hotdog.get_height() > HEIGHT:
                lives -= 1
                enemy.remove(hotdog)
        
        for fruit in foods[:]:
            fruit.move(fruit_vel)
            if collide(fruit, player):
                SCORE += 1
                foods.remove(fruit) 
            elif fruit.y + fruit.get_height() > HEIGHT:
                if SCORE != 0:
                    SCORE -= 1
                foods.remove(fruit)

        player.move_frisbee(-frisbee_vel, enemy)
        screen.fill(white)
        
# game_loop()