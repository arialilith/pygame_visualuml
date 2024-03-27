import pygame

class Button():
    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.rect.Rect((x, y),(150,25))
        self.clicked = False

    def draw(self, surface, font):
        action = False

        button_text = font .render(self.text, True, 'black')
        pygame.draw.rect(surface, 'light gray', self.rect, 0 ,5)
        pygame.draw.rect(surface, 'black', self.rect, 2, 5)

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False



        surface.blit(button_text, (self.rect.x, self.rect.y))

        return action