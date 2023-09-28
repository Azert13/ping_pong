#создай игру "Лабиринт"!
from pygame import*
window=display.set_mode((600,500))
window.fill((200, 255, 255))
display.set_caption('Лабиринт')
win_width=600
win_height=500


font.init()
font=font.SysFont('Arial',40)
lose1=font.render('Player1 LOSE!',True,(180,0,0))
lose2=font.render('Player2 LOSE!',True,(180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed,player_width,player_height):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (player_width,player_height))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys=key.get_pressed()
        if keys [K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys [K_DOWN] and self.rect.y<win_height-80:
            self.rect.y+=self.speed

    def update2(self):
        keys=key.get_pressed()
        if keys [K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys [K_s] and self.rect.y<win_height-80:
            self.rect.y+=self.speed

player1=Player("player.png",30,200,4,50,150)
player2=Player("player.png",520,200,4,50,150)
ball=GameSprite("ball.png",200,200,4,50,50)
clock = time.Clock()
game = True
finish=False
speed_x=4
speed_y=4
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish != True:
        window.fill((200,255,255))
        player1.update1()
        player2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *=-1
        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *=-1
        if ball.rect.x<0:
            finish=True
            window.blit(lose1,(200,200))
        if ball.rect.x>550:
            finish=True
            window.blit(lose2,(200,200))
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(60)
