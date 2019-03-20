import pygame
from  pygame.locals import *
import time,random
class Plane(object):
    def __init__(self,screen,x,y,image,image2):#初始化对象,自动调用
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image2 = image2
        self.screen = screen
        self.bullet_list = []
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        del_bullet_list = []
        for bulle in self.bullet_list:
            bulle.display()
            bulle.move()
            if bulle.judge == True:
                del_bullet_list.append(bulle)
        for num2 in del_bullet_list:
            self.bullet_list.remove(num2)
class Heroplane(Plane):
    def __init__(self,screen):#初始化对象,自动调用
        Plane.__init__(self,screen,210,600,"./feiji/hero2.png","./feiji/bullet.png")
    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def fire(self):   # !!! fire()函数把子弹和飞机的坐标联系在一起
        hero_bullet = HeroBullet(self.x, self.y, self.image2, self.screen)
        self.bullet_list.append(hero_bullet)
class Enenyplane(Plane):
    def __init__(self,screen):
        Plane.__init__(self,screen,0,0,"./feiji/enemy1.png","./feiji/bullet1.png")
        self.direction = "right"
    def move(self):
        if self.x <= 0:
            self.direction = "right"
        elif self.x >= 450:
            self.direction = "left"
        if self.direction == "right":
            self.x += 5
        else:
            self.x -= 5
    def fire(self):             # !!!
        num = random.randint(1,80)
        if num == 1 or num == 3 or num == 33 or num == 66:
            enemy_bullet = EnemyBullet(self.x, self.y, self.image2, self.screen)
            self.bullet_list.append(enemy_bullet)
class Bullet():
    def __init__(self,x,y,image,screen):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.screen = screen
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def judge(self):
        if self.y <= 0 or self.y >= 800:
            return True
        else:
            return False
class EnemyBullet(Bullet):
    def __init__(self,x,y,image,screen): #形参
        Bullet.__init__(self, x + 20, y+80, image, screen) #实参
    def move(self):
        self.y += 6
class HeroBullet(Bullet):
    def __init__(self,x,y,image,screen):
        Bullet.__init__(self,x+40,y,image,screen)
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
        hero.display()
        key_test(hero)
        enemy.display()
        enemy.move()
        enemy.fire()
        time.sleep(0.01)
        pygame.display.update()  # 更新显示界面
if __name__ == "__main__":
    main()
'''
飞机显示,子弹显示,背景显示
英雄飞机:键盘响应,坐标变化,图片显示位置变化,不断刷新
英雄子弹:键盘响应,fire方法创建子弹,存储在bullet_list,循环遍历列表,显示子弹,调用move()方法,每个子弹坐标变化,显示位置变化
敌机:判断self.direction,改变坐标
敌机子弹:通过随机数添加子弹至列表,循环遍历列表,显示子弹,调用move()方法,每个子弹坐标变化,显示位置变化
fire()方法把子弹和飞机坐标统一



'''