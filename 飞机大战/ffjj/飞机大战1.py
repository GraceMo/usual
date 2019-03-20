import pygame
from  pygame.locals import *
import time,random
class Heroplane():
    def __init__(self,screen):#初始化对象,自动调用
        self.x = 210
        self.y = 600
        self.image = pygame.image.load("./feiji/hero2.png")
        self.image2 = "./feiji/bullet.png"
        self.screen = screen
        self.bullet_list = []
    def display(self,enemy):
        self.screen.blit(self.image,(self.x,self.y))
        del_bullet_list = []
        for bulle in self.bullet_list:
            bulle.display()
            bulle.move()
           # enemy = Enenyplane(self.screen)
            if bulle.y <= 0:
                del_bullet_list.append(bulle)
            elif bulle.y <= 89:
                if enemy.x <= bulle.x <= enemy.x+69:
                    enemy.display(2)
        for num2 in del_bullet_list:
            self.bullet_list.remove(num2)
    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def fire(self):
        hero_bullet = Bullet(self.x, self.y, self.image2, self.screen)
        self.bullet_list.append(hero_bullet)
class Enenyplane():
    def __init__(self,screen):#初始化对象,自动调用
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./feiji/enemy1.png")
        self.image2 = "./feiji/bullet1.png"
        self.screen = screen
        self.bullet_list = []
        self.direction = "right"
        self.down1 = pygame.image.load("feiji/enemy1_down1.png")
        self.down2 = pygame.image.load("feiji/enemy1_down2.png")
        self.down3 = pygame.image.load("feiji/enemy1_down3.png")
        self.down4 = pygame.image.load("feiji/enemy1_down4.png")
        self.i = 0
        self.numb = 0
        self.down5 = pygame.image.load("feiji/quit_nor.png")
    def display(self,num = 0):#
        if  self.numb == num :
            self.screen.blit(self.image, (self.x, self.y))
            del_bullet_list = []
            for bulle in self.bullet_list:  # todo 1
                bulle.display()
                bulle.move()
                if bulle.y >= 800:
                   del_bullet_list.append(bulle)
            for num2 in del_bullet_list:
                self.bullet_list.remove(num2)
        else:
            self.numb = 2
            self.i += 1
            if self.i <= 10:
                self.screen.blit(self.down1, (self.x, self.y))
            elif self.i <= 30:
                self.screen.blit(self.down2, (self.x, self.y))
            elif self.i <= 45:
                self.screen.blit(self.down3, (self.x, self.y))
            elif self.i <= 60:
                self.screen.blit(self.down4, (self.x, self.y))
            elif self.i <= 75:
                quit()



    def move(self):
        if self.numb == 0:
            if self.x <= 0:
                self.direction = "right"
            elif self.x >= 450:
                self.direction = "left"
            if self.direction == "right":
                self.x += 5
            else:
                self.x -= 5
        else:
            self.x += 0
    def fire(self):
         if self.numb == 0:
            num = random.randint(1,100)
            if num == 1 or num == 3:
                enemy_bullet = EnemyBullet(self.x, self.y, self.image2, self.screen)
                self.bullet_list.append(enemy_bullet)
         else:
            pass
class EnemyBullet():
    def __init__(self,x,y,image,screen):
        self.x = x + 20
        self.y = y + 40
        self.image = pygame.image.load(image)
        self.screen = screen
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y += 6
def key_test(hero):#  定义带有参数的函数
   for event in pygame.event.get():  # 按键测试
       if event.type == QUIT:
           print("exit")
           exit()
       elif event.type == KEYDOWN:
           if event.key == K_LEFT:
               print("left")
               hero.move_left()
           elif event.key == K_RIGHT:
               print("right")
               hero.move_right()
           elif event.key == K_SPACE:
               print("space")
               hero.fire()
class Bullet():
    def __init__(self,x,y,image,screen):
        self.x = x + 40
        self.y = y
        self.image = pygame.image.load(image)
        self.screen = screen
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y -= 6
def key_test(hero):#  定义带有参数的函数
   for event in pygame.event.get():  # 按键测试
       if event.type == QUIT:
           print("exit")
           exit()
       elif event.type == KEYDOWN:
           if event.key == K_LEFT:
               print("left")
               hero.move_left()
           elif event.key == K_RIGHT:
               print("right")
               hero.move_right()
           elif event.key == K_SPACE:
               print("space")
               hero.fire()
def main():
    '''搭建界面,窗口和背景显示'''  # 通过不断的循环,达到效果
      #1,窗口
    screen = pygame.display.set_mode((480,852),0,32)
       #  2,窗口背景
    background = pygame.image.load("./feiji/background.png")
      #飞机对象
    hero = Heroplane(screen)
    enemy = Enenyplane(screen)
    while True:
           # 3,背景图和窗口组合,并显示飞机
        screen.blit(background,(0,0))
        hero.display(enemy)
        enemy.display()
        enemy.move()
        enemy.fire()
        key_test(hero)
        time.sleep(0.01)
        pygame.display.update()  # 更新显示界面

if __name__ == "__main__":
    main()