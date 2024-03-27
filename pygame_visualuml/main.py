import pygame
import button
import classobject

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 18)
pygame.display.set_caption("Visual UML")

active_box = None
boxes = []
def spawn_box():
    
    box = classobject.classbox(200,200, 200, 100)
    boxes.append(box)




button2 = button.Button("Object", 200, 10)
button = button.Button("Object", 10, 10)

run = True
while run:
    
    screen.fill('white')

    if button.draw(screen, font):
        spawn_box()

    if button2.draw(screen, font):
        print('Click2')

    for box in boxes:
        classobject.classbox.draw(box, screen, font)

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(boxes):
                    if box.rect.collidepoint(event.pos):
                        active_box = num
                    if box.text_box.collidepoint(event.pos):
                        box.active = True
                    else:
                        box.active = False
            

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None

        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes[active_box].rect.move_ip(event.rel)

        if event.type == pygame.KEYDOWN:
            print(event.unicode, event.unicode.isalpha())
            for num, box in enumerate(boxes):
                if event.unicode.isalpha() and box.active:
                    box.user_text = box.user_text + event.unicode
                if (event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE) and box.active:
                    box.user_text = box.user_text[:-1]
                print(box.user_text)

        if event.type == pygame.QUIT:
            run = False
    
    timer.tick(fps)
    pygame.display.update()
