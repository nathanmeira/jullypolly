import pygame, sys
import random
from pygame.locals import *
from game import Frisbee, Main, Player, Food

class FrisBol(object):   
    def __init__(self, width, height, screen):
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
        self.foods = []
        self.wave_length = 5
        self.food_vel = 1.5
        self.player_vel = 7
        self.frisbee_vel = 7
        self.x = (self.width * 0.45)
        self.y = (self.height * 0.78)
        self.lost = False
        self.lost_count = 0
        self.player = Player(self.x,self.y)
        
    def draw(self):
        self.screen.blit(self.BG, (0,0))
        lives_label = self.main_font.render(f"Lives: {self.lives}",1,(0,0,0))
        level_label = self.main_font.render(f"Level: {self.level}",1,(0,0,0))
        self.screen.blit(lives_label,(10,10))
        self.screen.blit(level_label,(self.width - level_label.get_width() - 10,10))

        for food in self.foods:
            food.draw(self.screen)
            
        self.player.draw(self.screen)

    def init(self):        
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(self.FPS)  
            self.draw()

            if self.lives <= 0:
                self.lost = True
                self.lost_count += 1

            if self.lost:
                if self.lost_count > self.FPS * 3:
                    self.run = False
                    break
                else:
                    continue

            if len(self.foods) == 0:
                self.level += 1
                self.wave_length += 5
                for i in range(self.wave_length):
                    food = Food(random.randrange(50, self.width-100), random.randrange(-1500, -100), random.choice(["carrot", "strawberry", "grape", "hotdog"]))
                    self.foods.append(food)

            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()  
            
            if keys[pygame.K_LEFT] and self.player.x - self.player_vel > 0:
                self.player.x -= self.player_vel 
            if keys[pygame.K_RIGHT] and self.player.x + self.player_vel + self.player.get_width() < self.width:
                self.player.x += self.player_vel
            if keys[pygame.K_SPACE]:
                self.player.shoot()

            for food in self.foods[:]:
                food.move(self.food_vel)
                if food.y + food.get_height() > self.height:
                    self.lives -= 1
                    self.foods.remove(food)

            self.player.move_frisbee(-self.frisbee_vel, self.foods)
            pygame.display.update()
        return False