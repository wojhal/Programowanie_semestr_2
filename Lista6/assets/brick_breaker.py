import pygame
import random
from operator import itemgetter
import json
import math

pygame.init()
pygame.font.init()
pygame.mixer.init()

# tworzenie okno
WIDTH, HEIGHT = 703, 770
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Footbrick Breaker")
font = pygame.font.Font("/Users/wojtek/Desktop/assets/street-cred/street cred.otf", 32)
font_przyciski = pygame.font.Font("/Users/wojtek/Desktop/assets/street-cred/street cred.otf", 28)
font_tytul = pygame.font.Font("/Users/wojtek/Desktop/assets/street-cred/street cred.otf", 40)
font_duzy = pygame.font.Font("/Users/wojtek/Desktop/assets/street-cred/street cred.otf", 50)
font_zasady = pygame.font.Font("/Users/wojtek/Desktop/assets/street-cred/street cred.otf", 25)
font_potezny = pygame.font.Font("/Users/wojtek/Desktop/assets/street-cred/street cred.otf", 80)
FPS = 60
PL_WIDTH = 100
PL_HEIGHT = 10
BALL_PR = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (50, 205, 50)
GREY = (105, 105, 105)
RED = (255, 0, 0)
ORANGE = (255,165,0)
SZAFIROWY = (15,82,186)
ICEBLUE = (135, 206, 235)
FIOLET = (75,0,130)
betis = "XXXXXXYXXXXXX\nYYYYYYGYYYYYY\nYGWGWGWGWGWGY\nYGWGWGGWWGWGY\nXYWGWGWGWGWYX\nXXYGWWGWWGYXX\nXXXYWGWGWYXXX\nXXXXYGWGYXXXX\nXXXXXYWYXXXXX\nXXXXXXYXXXXXX"
swansea = "XXXXXXWBBBXX\nXXXXXWBWWWBX\nXXXXXWBWWWBB\nXXXXXWWBWWWW\nXXXWWWWWBWXX\nXXWWBBBWBBWX\nXWWBBWWWWBBW\nXWBBWBBBWWBB\nBBBWBBWWWWWB\nWWWBBWBBBWWB\nWBBBWBBWWWBW\nXWWWBBWWBBWX\nXWBBBWWWWWWX"
hanover = "XXXGGGGGGXXXX\nXWBBBGGGGBBBW\nWBBBBBGGGBBBWX\nWBBWBBGGBBGGX\nWBBBBBGBBGGGX\nXGGBBBGBBBGGX\nXGGGBBGBBBBBW\nXGGBBGGBBWBBW\nXWBBBGGBBBBBW\nWBBBGGGGBBBWX\nXXXXGGGGGGXXX"
juve = "XXXWWWWWWXXX\nWWWBBBBWBWWW\nWWWWWWBWBWWW\nWWWWWWBWBWWW\nWWWWWWBWBWWW\nWWWWWWBWBWWW\nWWWWWBBWBWWW\nXWWWBBWWBWWX\nXXWWWWWBBWXX\nXXXWWWBBWXXX\nXXXXWBBWXXXX\nXXXXXWWXXXXX"
furth = "XXXXGGGGGXXXX\nXXGGWWWWWGGXX\nXGWWWGWGWWWGX\nXGWWGGGGGWWGX\nGWWGWGGGWGWWG\nGWGGGWGWGGGWG\nGWWGGGGGGGWWG\nGWGGGWGWGGGWG\nGWWGWWGWWGWWG\nXGWWWGGWWWWGX\nXGWWGGWWWWWGX\nXXGGWWWWWGGXX\nXXXXGGGGGXXXX"
wolves = "XXXXBBBBBXXXX\nXXXBOOOOOBXXX\nXXBOBOOOBOBXX\nXBOOBBBBBOOBX\nXBOBBBBBBBOBX\nBOOBBWBWBBOOB\nBOOOBBBBBOOOB\nXBOOOBBBOOOBX\nXBOOOBBBOOOBX\nXXBOOOBOOOBXX\nXXXBOOOOOBXXX\nXXXXBBBBBXXXX"
hamburg = "XXXXXXXXXXXXX\nSSSSSSSSSSSSS\nSSSSSSWSSSSSS\nSSSSSWWWSSSSS\nSSSSWBBBWSSSS\nSSSWWBWBWWSSS\nSSSSWBBBWSSSS\nSSSSSWWWSSSSS\nSSSSSSWSSSSSS\nSSSSSSSSSSSSS"
napoli = "XXXXSSSSSSSXXXX\nXXXSSSSSSSSSXXX\nXXSSSIIIIISSSXX\nXSSSIIIIIIISSSX\nSSSIWWIIWWWISSS\nSSIIIWWIIWIIISS\nSSIIIWWWIWIIISS\nSSIIIWIWIWIIISS\nSSIIIWIWWWIIISS\nSSIIIWIIWWIIISS\nSSSIWWWIIWIISSS\nXSSSIIIIIIISSSX\nXXSSSIIIIISSSXX\nXXXSSSSSSSSSXXX\nXXXXSSSSSSSXXXX"
hubi = 'XXXXXXXXXXXXXBB\nXXXXXXXXXXXXXBB\nXXXXXXXXXXXXXBB\nXXXXXXXXXXXXXBB\nXXXXXXXXBBBBBBBBBB'
viola = "XXXXXXFXXXXXX\nXXXXXFWFXXXXX\nXXXXFWRWFXXXX\nXXXFWRRRWFXXX\nXXFWRWRWRWFXX\nXFWWWRRRWWWFX\nFWFFWWRWWFFWF\nXFWFFFWFFFWFX\nXXFWFFFFFWFXX\nXXXFWFFFWFXXX\nXXXXFWFWFXXXX\nXXXXXFWFXXXXX\nXXXXXXFXXXXXX"
mapa = [betis, swansea, hanover, juve, furth, wolves, hamburg, napoli, hubi, viola]
lobby = "/Users/wojtek/Desktop/assets/mixkit-stadium-joy-shouting-crowd-3022.wav"
hicik = "/Users/wojtek/Desktop/assets/mixkit-arrow-shot-through-air-2771.wav"
hitens = "/Users/wojtek/Desktop/assets/mixkit-golf-ball-hit-2105.wav"
hicior = "/Users/wojtek/Desktop/assets/mixkit-basketball-ball-tap-2092.wav"
lamaga = "/Users/wojtek/Desktop/assets/mixkit-crowd-disappointment-long-boo-463.wav"
dzwieki = True

# platforma
class Platforma:
    """
    Klasa służąca do tworzenia obiektu Platformy (deski, którą kierujemy)

    Atrybuty:
    ----------
    x - float
        pozycja lewego górnego wierzchołka na mapie w poziomie
    y - float
        pozycja lewego górnego wierzchołka na mapie w pionie
    width - int
        szerokość platformy
    height - int
        wysokość platformy
    kolor - tuple
        kolor rgb platformy

    Metody:
    ---------
    poruszanie(kierunek)
        metoda pozwalająca na ruch platformą w zależności od parametru kierunku
    draw(SCREEN)
        metoda wyświetlająca platformę na ekranie (SCREEN)

    """
    VEL = 0

    def __init__(self, x, y, width, height, kolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.kolor = kolor

    def poruszanie(self, kierunek):
        self.x += self.VEL * kierunek

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, self.kolor, (self.x, self.y, self.width, self.height))


# piłka
class Ball:
    """
    Klasa służąca do tworzenia obiektu Piłki

    Atrybuty:
    ----------
    x - float
        pozycja środka piłki na mapie w poziomie
    y - float
        pozycja środka piłki na mapie w pionie
    r - float
        promień piłki
    x_vel - float
        prędkość z jaką porusza się piłka w poziomie
    y_vel - float
        prędkość z jaką porusza się piłka w pionie

    Metody:
    ---------
    poruszanie()
        metoda pozwalająca na ruch piłki po mapie oraz określająca jej ograniczenia
    draw(SCREEN)
        metoda wyświetlająca piłkęna ekranie razem z obrazkiem towarzyszącym

    """
    VEL = -4
    VEL1 = 5

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.x_vel = self.VEL1
        self.y_vel = self.VEL

    def poruszanie(self):
        self.x -= self.x_vel
        self.y += self.y_vel
        if self.x <= self.r or self.x >= WIDTH - self.r:
            self.x_vel = -1*self.x_vel
            if dzwieki == True:
                hicior_sound = pygame.mixer.Sound(hicior)
                pygame.mixer.Sound.play(hicior_sound)
        if self.y - self.r <= 0:
            self.y_vel = -1*self.y_vel
            if dzwieki == True:
                hicior_sound = pygame.mixer.Sound(hicior)
                pygame.mixer.Sound.play(hicior_sound)



    def draw(self, SCREEN):
        pilka = pygame.transform.scale(pygame.image.load("/Users/wojtek/Desktop/assets/ball.png"), (2*self.r, 2*self.r))
        pilka_rect = pilka.get_rect()
        pilka_rect.center = (self.x, self.y)
        pygame.draw.circle(SCREEN, WHITE, (self.x, self.y), self.r)
        SCREEN.blit(pilka, pilka_rect)

# klocki
class Brick:
    """
    Klasa służąca do tworzenia obiektów Klocków (bricków)

    Atrubuty:
    ----------
    x - float
        pozycja lewego górnego wierzchołka bricka na mapie w poziomie
    y - float
        pozycja lewego górnego wierzchołka bricka na mapie w pionie
    width - int
        szerokość bricka
    height - int
        wysokość bricka
    kolor - tuple
        kolor rgb bricka
    hit - bool
        definiuje czy blok został trafiony czy nie

    Metody:
    ---------
    draw(SCREEN)
        metoda do wyświetlania bricka na mapie

    """
    def __init__(self,x,y,width,height,kolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.kolor = kolor
        self.hit = False

    def draw(self, SCREEN):
            pygame.draw.rect(SCREEN, self.kolor, (self.x, self.y, self.width, self.height))



def tlo():
    """
    Funkcja służąca do ustawienia odpowiedniego tła dla każdego widoku z menu/gry

    """
    tlo = pygame.transform.scale(pygame.image.load("/Users/wojtek/Desktop/assets/peach.png"), (WIDTH, HEIGHT))
    pygame.display.flip()
    SCREEN.blit(tlo, (0, 0))

# zderzenie brick-pilka
def brick_pilka(brick, pilka):
    """
    Funkcja określająca moment zderzenia piłki z brickiem
    Parametry:
    ----------
    pilka - obiekt klasy Ball
    brick - obiekt klasy Brick
    Output:
    --------
    zmiana statusu obiektu brick hit na True (trafiony)

    """
    if brick.y <= pilka.y <= brick.y + brick.height and pilka.r >= brick.x - pilka.x > 0 or brick.y <= pilka.y <= brick.y + brick.height and pilka.r >= pilka.x - (brick.x+brick.width) > 0:
        pilka.x_vel = -1*pilka.x_vel
        brick.hit = True
    elif brick.x <= pilka.x <= brick.x+brick.width and pilka.r >= pilka.y - (brick.y+brick.height) > 0 or brick.x <= pilka.x <= brick.x+brick.width and pilka.r >= brick.y - pilka.y > 0:
        pilka.y_vel = -1*pilka.y_vel
        brick.hit = True

# generowanie mapy
def generowanie_mapy(mapa):
    """
    Funkcja służąca do wygenerowania mapy z jednego ze stringów podanych na początku (odpowiednie litery oznaczają odpowiedni kolor bricka)
    Parametry:
    ----------
    mapa - list
        lista map dostępnych do wygenerowania

    Output:
    ---------
    bricks_ele - list
        lista bricków, które są do zbicia na mapie

    """
    numer = random.randint(1, len(mapa))
    mapka = mapa[numer-1]
    bricks = [[*line.strip(',')] for line in mapka.split('\n') if line]
    gap = 3
    brick_width = WIDTH // len(bricks[0]) - gap
    brick_height = 30
    bricks_ele = []
    for rzedy in range(len(bricks)):
        for brick in range(len(bricks[rzedy])):
            if bricks[rzedy][brick] == "B":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, BLACK)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "G":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, GREEN)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "Y":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, YELLOW)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "W":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, WHITE)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "O":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, ORANGE)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "S":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, SZAFIROWY)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "I":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, ICEBLUE)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "F":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, FIOLET)
                bricks_ele.append(bricks[rzedy][brick])
            elif bricks[rzedy][brick] == "R":
                bricks[rzedy][brick] = Brick(brick * brick_width + (gap * brick+1), rzedy * brick_height + (gap * rzedy+1),
                                             brick_width, brick_height, RED)
                bricks_ele.append(bricks[rzedy][brick])


    return bricks_ele



# zderzenie platforma-pilka
def platforma_pilka(platforma, pilka):
    """
    Funkcja służąca do określenia momentu zderzenia piłki z platformą
    Parametry:
    ----------
    platforma - obiekt klasy Platforma
    pilka - obiekt klasy Ball

    Output:
    ---------
    odpowiednia zmiana kierunku piłki, w zależności od jej pozycji względem platformy w momencie uderzenia

    """
    if pilka.r + pilka.y == HEIGHT - 2 * platforma.height:
        punkt = round((pilka.x - platforma.x) / (platforma.width / 2), 1)
        if 0 <= punkt < 0.6 or 1.4 < punkt <= 2:
            pilka.x_vel = 2 * pilka.VEL1
        elif 0.6 <= punkt <= 1.4:
            pilka.x_vel = pilka.VEL1
        if platforma.x <= pilka.x < platforma.x + platforma.width / 2:
            if pilka.x_vel < 0:
                pilka.x_vel = -1 * pilka.x_vel
            pilka.y_vel = -1 * pilka.y_vel
        elif platforma.x + platforma.width / 2 < pilka.x <= platforma.x + platforma.width:
            if pilka.x_vel > 0:
                pilka.x_vel = -1 * pilka.x_vel
            pilka.y_vel = -1 * pilka.y_vel
        elif pilka.x == platforma.x + platforma.width/2:
            pilka.y_vel = -1 * pilka.y_vel
        if dzwieki == True:
            hitens_sound = pygame.mixer.Sound(hitens)
            pygame.mixer.Sound.play(hitens_sound)
    if HEIGHT - platforma.height <= pilka.y+pilka.r < HEIGHT:
        if pilka.r >= platforma.x - pilka.x > 0 and pilka.x_vel < 0 or \
                pilka.r >= pilka.x - (platforma.x+platforma.width) > 0 and pilka.x_vel > 0:
            pilka.x_vel = pilka.x_vel*-1

# okno
def wyglad_okna(platforma, pilka, bricks_ele, LIVES, WYNIK):
    """
    Funkcja służąca do przedstawienia wszystkich elementów na ekranie z rozgrywką oraz ich aktualizacja regularna
    Parametry:
    ----------
    platforma - obiekt klasy Platforma
    pilka - obiekt klasy Ball
    bricks_ele - list
        mapa bloków do zbicia
    LIVES - int
        liczba żyć przy jednym podejściu gracza
    WYNIK - int
        wynik gracza w pojedynczej rozgrywce

    Output:
    ---------
    przedstawienie wszystkich elementów na ekranie

    """
    tlo()
    platforma.draw(SCREEN)
    pilka.draw(SCREEN)
    for brick in bricks_ele:
        brick.draw(SCREEN)
    lives_text = font.render(f"Lives: {LIVES}", True, BLACK)
    SCREEN.blit(lives_text, (WIDTH-lives_text.get_width()-8, -5))
    lives_text = font.render(f'Lives: {LIVES}', True, WHITE)
    SCREEN.blit(lives_text, (WIDTH-lives_text.get_width()-10, -3))

    score_text = font.render(f'Score: {WYNIK}', True, BLACK)
    SCREEN.blit(score_text, (8, -5))
    score_text = font.render(f'Score: {WYNIK}', True, WHITE)
    SCREEN.blit(score_text, (10, -3))

# menu
class Przycisk:
    """
    Klasa służąca do reprezentacji przycisków w menu

    Atrybuty:
    ----------
    napis - string
        napis na przycisku
    pos - tuple
        pozycja przycisku na mapie
    button - obiekt Rect
        obiekt Rect, który posiada własne atrybuty np. kliknięcie

    Metody:
    ----------
    draw()
        metoda do wyśtwietlania przycisku z napisem na ekranie
    check_clicked()
        metoda sprawdzająca czy użytkownik wcisnął myszką pole przycisku

    """
    def __init__(self, napis, pos):
        self.napis = napis
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (240, 40))

    def draw(self):
        pygame.draw.rect(SCREEN, BLACK, self.button, 0, 5)
        pygame.draw.rect(SCREEN, WHITE, [self.pos[0], self.pos[1], 240, 40], 5, 5)
        text2 = font_przyciski.render(self.napis, True, WHITE)
        SCREEN.blit(text2, (self.button.midleft[0]+10, self.button.midleft[1]-15))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

# menu
def draw_menu():
    """
    Funkcja odpowiedzialna za stworzenie menu gry oraz "centrala do rozsyłania" gracza do odpowiednich okien np. samej rozgrywki, zasad

    Output:
    --------
    nieskończona pętla menu, chyba że zostaną przez gracza wciśnięte odpowiednie rzeczy (np. przycisk KONIEC GRY)

    """
    pygame.mixer.music.load(lobby)
    pygame.mixer.music.play(loops=-1)
    while True:
        tlo()
        tytul1 = pygame.draw.rect(SCREEN, WHITE, [140, 65, 423, 170], 5, 5)
        tytul = pygame.draw.rect(SCREEN, BLACK, (150, 75, 403, 150))
        txt = font_tytul.render('FOOT-BRICK BREAKER!', True, 'WHITE')
        SCREEN.blit(txt, (tytul1.x + 30, (tytul1.y + tytul1.height)/2))
        GRA = Przycisk('START', (232, 280))
        GRA.draw()
        ZASADY = Przycisk('ZASADY', (232, 345))
        ZASADY.draw()
        SCORES = Przycisk('NAJLEPSZE WYNIKI', (232, 410))
        SCORES.draw()
        AUTOR = Przycisk('O AUTORZE', (232, 475))
        AUTOR.draw()
        USTAWIENIA = Przycisk("USTAWIENIA", (232, 540))
        USTAWIENIA.draw()
        # menu exit button
        WYJSCIE = Przycisk('KONIEC GRY', (232, 605))
        WYJSCIE.draw()

        if WYJSCIE.check_clicked():
            pygame.quit()
        if ZASADY.check_clicked():
            zasady()
        if SCORES.check_clicked():
            scores()
        if AUTOR.check_clicked():
            autor()
        if USTAWIENIA.check_clicked():
            ustawienia()
        if GRA.check_clicked():
            draw_game()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

# zasady
def zasady():
    """
    Funkcja odpowiedzialna za okno zasad, ich przedstawienie w formie graficznej

    Output:
    ---------
    Nieskończona pętla okna zasad, chyba że zostaną przez gracza wciśnięte odpowiednie rzeczy (np.klawisz backspace)

    """
    running = True
    while running:
        tlo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_LEFT or event.key == pygame.K_BACKSPACE:
                    running = False
        zasady_tlo = pygame.draw.rect(SCREEN, WHITE, (60, 100, 583, 570))
        zasady_gry = font_duzy.render("ZASADY GRY:", True, BLACK)
        SCREEN.blit(zasady_gry, (210,100))
        pierwsza = font_przyciski.render("2.ZBIJAJ BLOKI I ZBIERAJ PUNKTY", True, BLACK)
        SCREEN.blit(pierwsza, (80, 300))
        druga = font_przyciski.render("3.NIE STRAĆ WSZYSTKICH ŻYĆ", True, BLACK)
        SCREEN.blit(druga, (80, 400))
        explain = font_zasady.render("1.RUSZAJ PLATFORMĄ LEWĄ I PRAWĄ STRZAŁKĄ", True, BLACK)
        SCREEN.blit(explain, (80, 200))
        zyczenia = font_duzy.render("MIŁEJ GRY :)", True, BLACK)
        SCREEN.blit(zyczenia, (210, 510))
    return

# o autorze
def autor():
    """
    Funkcja odpowiedzialna za dostarczenie informacji o autorze gry graczowi w formie graficznej

    Output:
    ---------
    Nieskończona pętla okna o autorze, chyba że zostaną przez gracza wciśnięte odpowiednie rzeczy (np.klawisz backspace)

    """
    running = True
    while running:
        tlo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_LEFT or event.key == pygame.K_BACKSPACE:
                    running = False
        autor_tlo = pygame.draw.rect(SCREEN, WHITE, (50, HEIGHT//2, 603, 60))
        autor_gry = font_duzy.render("ODDAŁ GRĘ 4 DNI PO CZASIE", True, BLACK)
        SCREEN.blit(autor_gry, (65, HEIGHT//2))

def zachowaj(highscores):
    """
    Funkcja służąca do modyfikacji pliku z najwyższymi wynikami z poziomu gry
    Parametry:
    ----------
    highscores - plik .json
        plik z zapisanymi najwyższymi wynikami w grze

    Output:
    ---------
    zapisanie danych w pliku z najwyższymi wynikami

    """
    with open('/Users/wojtek/Desktop/assets/highscore.json', 'w') as file:
        json.dump(highscores, file)


def laduj():
    """
    Funkcja odpowiedzialna za załadowanie/utworzenie (jeśli takowy nie istnieje) pliku z najwyższymi wynikami do wyświetlenia/modyfikacji ich

    Output:
    ---------
    posortowana od najwyższego lista z najwyższymi wynikami

    """
    try:
        with open('/Users/wojtek/Desktop/assets/highscore.json', 'r') as file:
            highscores = json.load(file)
    except FileNotFoundError:
        return []
    return sorted(highscores, key=itemgetter(1), reverse=True)

def scores():
    """
    Funkcja odpowiedzialna za dostarczenie informacji graczowi o  makysmalnie 5 najwyższych wynikach uzyskanych
    zapisanych w pliku .json

    Output:
    ---------
    Nieskończona pętla okna z najwyższymi wynikami, chyba że zostaną przez gracza wciśnięte odpowiednie rzeczy
    (np.klawisz backspace)

    """
    running = True
    while running:
        tlo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_LEFT or event.key == pygame.K_BACKSPACE:
                    running = False
        highscore1 = font_potezny.render('NAJLEPSZE WYNIKI', True, BLACK)
        SCREEN.blit(highscore1, (highscore1.get_width() // 12-3, 42))
        highscore2 = font_potezny.render('NAJLEPSZE WYNIKI', True, WHITE)
        SCREEN.blit(highscore2, (highscore2.get_width() // 12, 40))
        highscores = laduj()
        for y, (high_name, high_score) in enumerate(highscores):
            tekst1 = font_potezny.render(f'{high_name}:{high_score}', True, BLACK)
            SCREEN.blit(tekst1, (47, 152+y*100))
            tekst2 = font_potezny.render(f'{high_name}:{high_score}', True, WHITE)
            SCREEN.blit(tekst2, (50, 150+y*100))

def ustawienia():
    """
    Funkcja odpowiedzialna za okno ustawienia, w którym gracz może wyłączyć lub ponownie włączyć dźwięk na poziomie całej gry

    Output:
    ---------
    Zmodyfikowany lub nie dźwięk oraz nieskończona pętla okna ze zmianą dźwięku, chyba że zostaną przez gracza wciśnięte
     odpowiednie rzeczy (np.klawisz backspace)

    """
    global dzwieki
    running = True
    while running:
        tlo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_LEFT or event.key == pygame.K_BACKSPACE:
                    running = False
                if event.key == pygame.K_q:
                    if dzwieki:
                        pygame.mixer.music.pause()
                        dzwieki = False
                    elif not dzwieki:
                        pygame.mixer.music.unpause()
                        dzwieki = True

        dzwiek_tlo = pygame.draw.rect(SCREEN, WHITE, (60, 100, 583, 570))
        dzwiek_gry = font_potezny.render("DŹWIĘK", True, BLACK)
        dzwiek_wylacz = font_duzy.render("WCIŚNIJ 'Q' ŻEBY WYŁĄCZYĆ", True, BLACK)
        dzwiek_wylacz2 = font_duzy.render("DŹWIĘK", True, BLACK)
        SCREEN.blit(dzwiek_gry, (210, 100))
        SCREEN.blit(dzwiek_wylacz, (63, 300))
        SCREEN.blit(dzwiek_wylacz2, (265, 360))



# gra
def draw_game():
    """
    Funkcja odpowiedzialna za wyświetlanie oraz utrzymywanie rozgrywki w pętli dopóki gracz nie straci wszystkich żyć.
    Domyślnie włączone są dźwięki przy zderzeniu piłki ze ścianami, brickami i platformą, wyłączone, jeśli taka
    modyfikacja zostanie dokonana wcześniej w ustawieniach. Jeśli gracz zbije wszystkie bloki zostaje my wylosowana mapa
    z listy wszystkich map (może być ta sama). Po zdobyciu 250 puntków oraz ich wielokrotności (500,750,itd.) zwiększana
    jest progresywnie szybkość piłki, co wpływa na trudność rozgrywki. Jeśli wszystkie życia zostaną utracone, pojawia się
    ekran wyjścia z komunikatem informującym gracza o przeganej, który może dalej przejść w ekran wpisywania nazwy, gdzie
    podaje się nazwę do umieszczenia w najwyższych wynikach, jeśli wynik rozgrywki jest większy niż 5. najwyższy wynik

    Output:
    ---------
    W zależności od zachowania użytkownika okno gry można opuścić automatycznie (wciskając czerwonego "x" u góry okna gry)
    lub grać dalej i próbować przebić się do 5. najwyższych wyników. Wszystkie okna działające w tej funkcji to nieskoń-
    czone pętle, które, podobnie jak okno gry opisane powyżej można opuścić i wrócić do menu

    """
    global highscores
    if dzwieki == True:
        pygame.mixer.music.pause()
    active = False
    platforma = Platforma(WIDTH // 2 - PL_WIDTH // 2, HEIGHT - 2 * PL_HEIGHT, PL_WIDTH, PL_HEIGHT, ORANGE)
    pilka = Ball(BALL_PR+1, HEIGHT - BALL_PR, BALL_PR)
    bricks_ele = generowanie_mapy(mapa)
    WYNIK = 0
    LIVES = 3
    pilka.x_vel = 0
    pilka.y_vel = 0
    clock = pygame.time.Clock()
    running = True
    bez_zyc = False
    wynikanie = False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not active:
                    active = True
                    pilka.x_vel = pilka.VEL1
                    pilka.y_vel = pilka.VEL
                    platforma.VEL = 7
        pilka.poruszanie()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and platforma.x - platforma.VEL >= 0:  # LEFT
            platforma.poruszanie(-1)
        if keys_pressed[pygame.K_RIGHT] and platforma.x + platforma.VEL <= WIDTH - platforma.width:  # RIGHT
            platforma.poruszanie(1)
        platforma_pilka(platforma, pilka)
        for brick in bricks_ele:
            brick_pilka(brick, pilka)
            if brick.hit:
                if dzwieki == True:
                    hicik_sound = pygame.mixer.Sound(hicik)
                    pygame.mixer.Sound.play(hicik_sound)
                bricks_ele.remove(brick)
                WYNIK += 5
                if WYNIK % 250 == 0 and WYNIK != 0 and WYNIK <= 1000:
                    pilka.VEL1 += 0.5
        if not bricks_ele:
            platforma.x = WIDTH // 2 - PL_WIDTH // 2
            pilka.x = WIDTH // 2
            pilka.y = HEIGHT - 2* PL_HEIGHT - BALL_PR
            pilka.x_vel = pilka.VEL1
            pilka.y_vel = pilka.VEL
            bricks_ele = generowanie_mapy(mapa)
        if pilka.y > HEIGHT and bricks_ele:
            LIVES -= 1
            platforma.x = WIDTH // 2 - PL_WIDTH // 2
            pilka.x = WIDTH // 2
            pilka.y = HEIGHT - 2 * PL_HEIGHT - BALL_PR
            pilka.x_vel = pilka.VEL1
            pilka.y_vel = pilka.VEL
        wyglad_okna(platforma, pilka, bricks_ele, LIVES, WYNIK)
        if not active:
            press_space = font_tytul.render('NACIŚNIJ SPACJE ABY ZAGRAĆ', True, BLACK)
            SCREEN.blit(press_space, (press_space.get_width()//4-3, 497))
            press_space2 = font_tytul.render('NACIŚNIJ SPACJE ABY ZAGRAĆ', True, RED)
            SCREEN.blit(press_space2, (press_space.get_width() // 4, 500))
        if LIVES == 0:
            bez_zyc = True
            running = False
            if dzwieki == True:
                slabiak = pygame.mixer.Sound(lamaga)
                pygame.mixer.Sound.play(slabiak)
    while bez_zyc:
        tlo()
        informacja = font_potezny.render('PRZEGRAłEŚ :(', True, BLACK)
        SCREEN.blit(informacja, (WIDTH // 6, HEIGHT // 2 - informacja.get_height()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bez_zyc = False
                if dzwieki == True:
                    pygame.mixer.Sound.set_volume(slabiak, 0.0)
                    pygame.mixer.music.unpause()
            if event.type == pygame.KEYDOWN:
                highscores = laduj()
                if highscores == [] or WYNIK > highscores[-1][1]:
                    bez_zyc = False
                    wynikanie = True
                    if dzwieki == True:
                        pygame.mixer.Sound.set_volume(slabiak, 0.0)
                        pygame.mixer.music.unpause()
                else:
                    bez_zyc = False
    aktywnosc = False
    while wynikanie:
        tlo()
        if not aktywnosc:
            text = ''
        imie1 = font_tytul.render('WPISZ SWOJĄ NAZWĘ:', True, BLACK)
        SCREEN.blit(imie1, (WIDTH//5-3, HEIGHT//2-48))
        imie2 = font_tytul.render('WPISZ SWOJĄ NAZWĘ:', True, WHITE)
        SCREEN.blit(imie2, (WIDTH//5, HEIGHT//2-50))
        input_rect = pygame.Rect(WIDTH//5+20, HEIGHT//2, WIDTH//2, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wynikanie = False
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_RETURN:
                    aktywnosc = True
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) <= 15:
                            text += event.unicode
                else:
                    highscores.append([text, WYNIK])
                    highscores = sorted(highscores, key=itemgetter(1), reverse=True)
                    if len(highscores) > 5:
                        highscores.pop()
                    zachowaj(highscores)
                    aktywnosc = False
                    wynikanie = False

        pygame.draw.rect(SCREEN, WHITE, input_rect)
        dane_gracza = font_przyciski.render(text, True, RED)
        SCREEN.blit(dane_gracza, (input_rect.x+10, input_rect.y+30))
        pygame.display.flip()

def main():
    """
    Funkcja służąca do wywołania całej gry, ze wszystkimi elementami

    Output:
    ---------
    Gra FootBrick Breaker

    """
    draw_menu()

main()
