import pygame, sys
import random
from pygame.locals import *
from game import Frisbee, Main, Player, Food

class FrisBol(object):   
    def __init__(self, width, height, screen, jully):
        self.SCORE = 0
        self.width = width
        self.height = height
        self.screen = screen
        self.BG = pygame.transform.scale(pygame.image.load('personagem/imagens/background.png'), (self.width, self.height))
        self.white = (255,255,255)
        self.run = True
        self.FPS = 60
        self.level = 0
        self.lives = 3
        self.main_font = pygame.font.SysFont("comicsans",50)
        self.lost_font = pygame.font.SysFont("comicsans",60)
        self.enemy = []
        self.foods = [] 
        self.wave_length = 5
        self.enemy_vel = 1.5
        self.fruit_vel = 2
        self.vel_x = 10
        self.jump_y = 15
        self.jump = False
        self.player_vel = 7
        self.frisbee_vel = 7
        self.x = (self.width * 0.45)
        self.y = (self.height * 0.78)
        self.lost = False
        self.lost_count = 0
        self.player = Player(self.x,self.y)
        self.jully = jully
        
    def draw(self):
        self.screen.blit(self.BG, (0,0))
        lives_label = self.main_font.render(f"Vidas: {self.lives}",1,(0,0,0))
        level_label = self.main_font.render(f"Level: {self.level}",1,(0,0,0))
        score_label = self.main_font.render(f"Pontos: {self.SCORE}",1,(0,0,0))
        self.screen.blit(lives_label,(10,10))
        self.screen.blit(score_label,(10,60))
        self.screen.blit(level_label,(self.width - level_label.get_width() - 10,10))

        for hotdog in self.enemy:
            hotdog.draw(self.screen)
        for fruit in self.foods:
            fruit.draw(self.screen)

        self.player.draw(self.screen)

    def collide(self, obj1, obj2):
        offset_x = (int(obj2.x - obj1.x))
        offset_y = (int(obj2.y - obj1.y))
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    def init(self):        
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(self.FPS)  
            self.draw()

            if self.lives <= 0:
                self.lost = True
                self.lost_count += 1

            if self.lost:
                if self.lost_count:
                    self.run = False
                    break
                else:
                    continue

            if len(self.enemy) == 0:
                self.level += 1
                self.wave_length += 2
                self.enemy_vel += 0.2
                for i in range(self.wave_length):
                    hotdog = Food(random.randrange(50, self.width-100), random.randrange(-1500, -100), "hotdog")
                    fruit = Food(random.randrange(50, self.width-100), random.randrange(-1500, -100), random.choice(["carrot", "strawberry", "grape"]))
                    self.enemy.append(hotdog)
                    self.foods.append(fruit) 

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT or keys[pygame.K_ESCAPE]:
                    self.run = False
            if keys[pygame.K_a] or keys[pygame.K_LEFT] and self.player.x - self.vel_x > 0:
                self.player.x -= self.vel_x 
            if keys[pygame.K_d] or keys[pygame.K_RIGHT] and self.player.x + self.vel_x + self.player.get_width() < self.width:
                self.player.x += self.vel_x
            if keys[pygame.K_SPACE]:
                self.player.shoot()

            if self.jump is False and keys[pygame.K_w] or keys[pygame.K_UP]:
                self.jump = True

            if self.jump is True:
                self.player.y -= self.jump_y
                self.jump_y -= 1
                if self.jump_y < -15:
                    self.jump = False
                    self.jump_y = 15

            for hotdog in self.enemy[:]:
                hotdog.move(self.enemy_vel)
                if self.collide(hotdog, self.player):
                    self.lives -= 1
                    self.enemy.remove(hotdog)
                elif hotdog.y + hotdog.get_height() > self.height:
                    self.lives -= 1
                    self.enemy.remove(hotdog)

            for fruit in self.foods[:]:
                fruit.move(self.fruit_vel)
                if self.collide(fruit, self.player):
                    self.SCORE += 1
                    self.jully.addStatusVida(fruit.type)
                    self.foods.remove(fruit) 
                elif fruit.y + fruit.get_height() > self.height:
                    if self.SCORE != 0:
                        self.SCORE -= 1
                    self.foods.remove(fruit)

            self.player.move_frisbee(-self.frisbee_vel, self.enemy, self.jully)
            pygame.display.update()
        return False