import sys
import random
import asyncio
import pygame
from pygame import mixer
from pygame.locals import *

pygame.init()
pygame.mixer.init()
# play = True

# Set the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set the background color
BACKGROUND_COLOR = (0, 0, 0)

# Set the font
FONT = pygame.font.Font(None, 64)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 25)

# Set the text for the game over message
GAME_OVER_TEXT = "Game Over!"

# Set the position for the game over message


# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Game Over")

# Loop until the user clicks the close button
done = False

# Create a clock to control the frame rate
clock = pygame.time.Clock()

''' Images '''
player1 = 'R7.png'
musuh1 = 'R4.png'
musuh2 = 'R8.png'
peluru_player = 'R3.png'
peluru_musuh = 'R5.png'
powerup_1 = 'power1.png'
apa = 2
ini = 10
iya = 2

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen2 = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
s_width, s_height = screen.get_size()
GAME_OVER_POSITION = (s_width // 2, s_height // 2)
GAME_OVER_POSITION2 = (s_width // 2, (2 * s_height) // 3)
GAME_OVER_POSITION3 = (s_width//2, (4 * s_height) // 5)


clock = pygame.time.Clock()
FPS = 40

# mengelompokkan efek bintang di background
background_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
musuh_group = pygame.sprite.Group()
musuh2_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()
peluruplayer_group = pygame.sprite.Group()
pelurumusuh_group = pygame.sprite.Group()
powerup_group = pygame.sprite.Group()
powerup2_group = pygame.sprite.Group()
powerup3_group = pygame.sprite.Group()

# membuat bintang di background


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([x, y])
        self.image.fill('white')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()

        # kecepatan bintang dan posisinya

    def update(self):
        self.rect.y += 1
        self.rect.x += 1
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(-400, s_width)


class PeluruPlayer(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')

    def update(self):
        self.rect.y -= 30  # kecepatan peluru
        if self.rect.y < 0:
            self.kill()


class PeluruMusuh(PeluruPlayer):
    def __init__(self, img):
        super().__init__(img)

    def update(self):
        self.rect.y += 7
        self.rect.x += 1
        if self.rect.y > s_height:
            self.kill()


class PeluruMusuh2(PeluruPlayer):
    def __init__(self, img):
        super().__init__(img)

    def update(self):
        self.rect.y += 7
        self.rect.x -= 1
        if self.rect.y > s_height:
            self.kill()


class PeluruMusuh3(PeluruPlayer):
    def __init__(self, img):
        super().__init__(img)

    def update(self):
        self.rect.y -= 7
        self.rect.x += 1
        if self.rect.y > s_height:
            self.kill()


class PeluruMusuh4(PeluruPlayer):
    def __init__(self, img):
        super().__init__(img)

    def update(self):
        self.rect.y -= 7
        self.rect.x -= 1
        if self.rect.y > s_height:
            self.kill()


class PeluruMusuh5(PeluruPlayer):
    def __init__(self, img):
        super().__init__(img)

    def update(self):
        self.rect.y -= 40
        self.rect.x += 5
        if self.rect.y > s_height:
            self.kill()


class PeluruMusuh6(PeluruPlayer):
    def __init__(self, img):
        super().__init__(img)

    def update(self):
        self.rect.y -= 40
        self.rect.x -= 5
        if self.rect.y > s_height:
            self.kill()


class Powerup1(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, (s_width-100))
        self.image.set_colorkey('black')

    def update(self):
        self.rect.y += 15
        if self.rect.y > s_height:
            self.rect.x = random.randrange(100, (s_width-100))
            self.rect.y = random.randrange(-3000, -200)


class Powerup2(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, (s_width-100))
        self.image.set_colorkey('black')

    def update(self):
        self.rect.y += 15
        if self.rect.y > s_height:
            self.rect.x = random.randrange(100, (s_width-100))
            self.rect.y = random.randrange(-3000, -200)


class Powerup3(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, (s_width-100))
        self.image.set_colorkey('black')

    def update(self):
        self.rect.y += 15
        if self.rect.y > s_height:
            self.rect.x = random.randrange(100, (s_width-100))
            self.rect.y = random.randrange(-3000, -200)


class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self. image.get_rect()
        self.image.set_colorkey('black')

    def update(self):
        gerak = pygame.mouse.get_pos()
        self.rect.x = gerak[0]
        self.rect.y = gerak[1]

    def shoot(self):
        peluru = PeluruPlayer(peluru_player)
        mouse = pygame.mouse.get_pos()
        peluru.rect.x = mouse[0] + 20
        peluru.rect.y = mouse[1] - 15
        # suara = mixer.Sound('laser2.wav')
# suara.set_volume(0.1)
# suara.play()
        peluruplayer_group.add(peluru)
        sprite_group.add(peluru)

    def shoot2(self):
        peluru1 = PeluruMusuh5(peluru_player)
        mouse = pygame.mouse.get_pos()
        peluru1.rect.x = mouse[0] + 20
        peluru1.rect.y = mouse[1] - 10
        # suara = mixer.Sound('laser2.wav')
# suara.set_volume(0.1)
# suara.play()
        peluruplayer_group.add(peluru1)
        sprite_group.add(peluru1)

    def shoot3(self):
        peluru11 = PeluruMusuh6(peluru_player)
        mouse = pygame.mouse.get_pos()
        peluru11.rect.x = mouse[0] + 20
        peluru11.rect.y = mouse[1] - 10
        # suara = mixer.Sound('laser2.wav')
# suara.set_volume(0.1)
# suara.play()
        peluruplayer_group.add(peluru11)
        sprite_group.add(peluru11)


class Musuh(Player):

    def __init__(self, img):
        super().__init__(img)
        self.rect.x = random.randrange(0, (s_width-100))
        self.rect.y = random.randrange(-500, 0)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += apa
        if self.rect.y > s_height:
            self.rect.x = random.randrange(100, (s_width-100))
            self.rect.y = random.randrange(-200, 0)
        self.shoot()

    def shoot(self):
        if self.rect.y in (50, 100, 150, 300, 350, 400):
            peluru2 = PeluruMusuh(peluru_musuh)
            peluru2.rect.x = self.rect.x + 15
            peluru2.rect.y = self.rect.y + 15
            peluru3 = PeluruMusuh2(peluru_musuh)
            peluru3.rect.x = self.rect.x + 15
            peluru3.rect.y = self.rect.y + 15
            suara = pygame.mixer.Sound('laser.wav')
            suara.set_volume(0.05)
            suara.play()
            pelurumusuh_group.add(peluru2, peluru3)
            sprite_group.add(peluru2, peluru3)

        elif self.rect.y in (500, 550, 600, 650, 700, 750):
            peluru4 = PeluruMusuh3(peluru_musuh)
            peluru4.rect.x = self.rect.x + 15
            peluru4.rect.y = self.rect.y + 15
            peluru5 = PeluruMusuh4(peluru_musuh)
            peluru5.rect.x = self.rect.x + 15
            peluru5.rect.y = self.rect.y + 15
            suara = pygame.mixer.Sound('laser.wav')
            suara.set_volume(0.05)
            suara.play()
            pelurumusuh_group.add(peluru4, peluru5)
            sprite_group.add(peluru4, peluru5)


class Musuh2(Musuh):

    def __init__(self, img):
        super().__init__(img)
        self.rect.x = random.randrange(0, (s_width-300))
        self.rect.y = random.randrange(-500, 0)

    def update(self):
        self.rect.y += 10
        if self.rect.y > s_height/3:
            self.rect.y -= 10
            self.rect.x += 2
            self.shoot()
        if self.rect.x > s_width:
            self.rect.x *= -1
        self.shoot()

    def shoot(self):
        if self.rect.x in (0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1050):
            peluru2 = PeluruMusuh(peluru_musuh)
            peluru2.rect.x = self.rect.x + 100
            peluru2.rect.y = self.rect.y + 100
            peluru3 = PeluruMusuh2(peluru_musuh)
            peluru3.rect.x = self.rect.x + 100
            peluru3.rect.y = self.rect.y + 100
            peluru4 = PeluruMusuh3(peluru_musuh)
            peluru4.rect.x = self.rect.x + 100
            peluru4.rect.y = self.rect.y - 10
            peluru5 = PeluruMusuh4(peluru_musuh)
            peluru5.rect.x = self.rect.x + 100
            peluru5.rect.y = self.rect.y - 10
            suara = pygame.mixer.Sound('laser.wav')
            suara.set_volume(0.05)
            suara.play()
            pelurumusuh_group.add(peluru2, peluru3)
            sprite_group.add(peluru2, peluru3, peluru4, peluru5)


class Game:
    def __init__(self):
        self.count_hit = 0
        self.count_hit2 = 0
        self.lives = 5
        self.score = 0
        self.tm = 0
        self.pull = 1
        self.tunggu = 0
        self.waktu = 0
        self.collap = False
        self.run_game()

    mixer.music.load('ini.wav')
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    pygame.mouse.set_cursor(
        (8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

    # def over_text(self):
# font = pygame.font.SysFont('Calibri', 50)
# text = font.render('GAME OVER', True, 'white')
# text_rect =	text.get_rect(center=(s_width/2, s_height/2))
# screen.blit(text, text_rect)

    def gameover(self):
        while not done:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        pygame.quit()
                        sys.exit()

    # Clear the screen
            window.fill(BACKGROUND_COLOR)

    # Draw the game over message
            text = FONT.render(GAME_OVER_TEXT, True, 'white')
            text2 = font2.render(
                'Skor kamu: ' + str(self.score), True, 'white')
            text3 = font3.render('Tekan enter untuk keluar', True, 'white')
            text_rect = text.get_rect(center=GAME_OVER_POSITION)
            text_rect2 = text2.get_rect(center=GAME_OVER_POSITION2)
            text_rect3 = text2.get_rect(center=GAME_OVER_POSITION3)
            window.blit(text, text_rect)
            window.blit(text2, text_rect2)
            window.blit(text3, text_rect3)

    # Update the display
            pygame.display.update()

    # Control the frame rate
            clock.tick(60)

    def create_background(self):
        for i in range(30):
            x = random.randint(1, 6)
            background_image = Background(x, x)
            background_image.rect.x = random.randrange(0, s_width)
            background_image.rect.y = random.randrange(0, s_height)
            background_group.add(background_image)
            sprite_group.add(background_image)

    def create_player(self):
        self.player = Player(player1)
        player_group.add(self.player)
        sprite_group.add(self.player)

    def create_musuh(self):
        for i in range(3):
            self.musuh = Musuh(musuh1)
            musuh_group.add(self.musuh)
            sprite_group.add(self.musuh)

    def create_musuh2(self):
        for i in range(1):
            self.musuh21 = Musuh2(musuh2)
            musuh2_group.add(self.musuh21)
            sprite_group.add(self.musuh21)

    def create_powerup1(self):
        for i in range(1):
            self.powerup11 = Powerup1(powerup_1)
            powerup_group.add(self.powerup11)
            sprite_group.add(self.powerup11)

    def create_powerup2(self):
        for i in range(1):
            self.powerup12 = Powerup2(powerup_1)
            powerup2_group.add(self.powerup12)
            sprite_group.add(self.powerup12)

    def create_powerup3(self):
        for i in range(1):
            self.powerup13 = Powerup3(powerup_1)
            powerup3_group.add(self.powerup13)
            sprite_group.add(self.powerup13)

    def hit_musuh(self):
        hits = pygame.sprite.groupcollide(
            musuh_group, peluruplayer_group, False, True)
        for i in hits:
            self.count_hit += 1
            suara = pygame.mixer.Sound('kena.wav')
            suara.set_volume(0.05)
            suara.play()
            if self.count_hit == 20:
                i.rect.x = random.randrange(0, (s_width-400))
                i.rect.y = random.randrange(-500, 0)
                self.score += 13
                self.count_hit = 0

    def hit_musuh2(self):
        hits = pygame.sprite.groupcollide(
            musuh2_group, peluruplayer_group, False, True)
        for i in hits:
            self.count_hit2 += 1
            suara = pygame.mixer.Sound('kena.wav')
            suara.set_volume(0.05)
            suara.play()
            if self.count_hit2 == 400:
                i.rect.x = s_width/2
                i.rect.y = random.randrange(-700, -200)
                self.score += 20
                self.count_hit2 = 0

    def hit_player(self):
        hits = pygame.sprite.groupcollide(
            player_group, pelurumusuh_group, self.collap, True)
        if hits:
            self.lives -= 1

    def hit_player2(self):
        hits = pygame.sprite.groupcollide(
            player_group, musuh_group, self.collap, True)
        if hits:
            self.lives -= 2
            self.score += 13

    def hit_player3(self):
        hits = pygame.sprite.groupcollide(
            player_group, musuh2_group, self.collap, True)
        if hits:
            self.lives -= 3
            self.score += 13
            self.tm = 1

    def hit_powerup1(self):
        hits = pygame.sprite.groupcollide(
            player_group, powerup_group, False, True)
        if hits:
            self.pull = 4
            suara = pygame.mixer.Sound('reload.wav')
            suara.set_volume(0.05)
            suara.play()

    def hit_powerup2(self):
        hits = pygame.sprite.groupcollide(
            player_group, powerup2_group, False, True)
        if hits:
            self.pull = 5
            suara = pygame.mixer.Sound('reload.wav')
            suara.set_volume(0.05)
            suara.play()

    def hit_powerup3(self):
        hits = pygame.sprite.groupcollide(
            player_group, powerup3_group, False, True)
        if hits:
            self.lives += 1
            self.pull = 6
            suara = pygame.mixer.Sound('reload.wav')
            suara.set_volume(0.05)
            suara.play()

    def nyawa(self):
        self.nyawa1 = pygame.image.load(player1)
        self.nyawa1 = pygame.transform.scale(self.nyawa1, (15, 40))
        n = 0
        for i in range(self.lives):
            screen.blit(self.nyawa1, (20+n, 25))
            n += 30

    def score1(self):
        nilai = self.score
        font = pygame.font.SysFont('Verdana', 20)
        text = font.render('Skor: '+str(nilai), True, 'white')
        text_rect = text.get_rect(center=(s_width-200, 50))
        screen.blit(text, text_rect)

    def run_update(self):
        sprite_group.draw(screen)
        sprite_group.update()

    def power(self):
        if self.pull == 1:
            self.pull = 0
            self.create_powerup1()
        elif self.pull == 2:
            self.pull = 0
            self.create_powerup2()
        elif self.pull == 3:
            self.pull = 0
            self.create_powerup3()

        if self.pull == 4:
            self.waktu += 1
            if self.waktu <= 500:
                self.player.shoot()

            elif self.waktu > random.randrange(700, 1000):
                self.pull = random.randint(1, 3)
                self.waktu = 0

        elif self.pull == 5:
            self.waktu += 1
            if self.waktu <= 500:
                self.player.shoot2()
                self.player.shoot3()

            elif self.waktu > random.randrange(700, 1000):
                self.pull = random.randint(1, 3)
                self.waktu = 0

        elif self.pull == 6:
            self.waktu += 1
            if self.waktu > 100:
                self.pull = random.randint(1, 2)
                self.waktu = 0

        # membuat tobol quit

    async def run_game(self):
        self.create_background()
        self.create_player()

        while True:
            screen.fill('black')
            self.run_update()
            self.hit_musuh()
            self.hit_musuh2()
            self.hit_powerup1()
            self.hit_powerup2()
            self.hit_powerup3()
            self.hit_player3()
            self.hit_player()
            self.hit_player2()
            self.power()
            pygame.draw.rect(screen, 'black', (0, 0, s_width, 100))
            self.nyawa()
            self.score1()
            patokan = random.randint(1200, 2000)

            if self.score >= 0 and self.score < 100:
                if self.tm == 0:
                    self.tm = 1
                    self.create_musuh()

            if self.score > 100 and self.score < 400:
                if self.tm == 1:
                    self.tm = 2
                    self.create_musuh2()
                    global apa
                    apa = 5

            if self.score > 400 and self.score < 800:
                if self.tm == 2:
                    self.tm = 3
                    self.create_musuh()
                    self.create_musuh2()
                    global ini
                    global iya
                    ini = 15
                    iya = 5

            if self.score > 800 and self.score < patokan:
                if self.tm == 3:
                    self.tm = 0
                    self.create_musuh()
                    self.create_musuh2()
                    apa = 8
                    ini = 20
                    iya = 8

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        pygame.quit()
                        sys.exit()

            if self.lives == 0:
                self.gameover()
                mixer.music.play(0)

            
            pygame.display.update()
            clock.tick(FPS)
            await asyncio.sleep(0)
    

if __name__ == '__main__':
    game = Game()
    asyncio.run(game.run_game())
