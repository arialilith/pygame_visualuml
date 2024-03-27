import pygame


class classbox():

    def __init__(self, x, y, w, h):
        self.user_text = ['Class']
        self.cursor = 0
        self.active = True
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect((self.x, self.y),(self.w,self.h))
        self.text_box = pygame.Rect(self.x,self.y,100,30)

    def draw(self, surface, font):

        if self.active:
            boxColor = 'white'
        else:
            boxColor = 'grey'


            
        pygame.draw.rect(surface, 'light gray', self.rect, 0, 5)
        pygame.draw.rect(surface, 'black', self.rect, 2, 5)


        def draw_text(text, font, x, y):
            img = font.render(text, True, 'black')
            width = img.get_width()
            surface.blit(img, (x+5, y+5))
        


        textBox = pygame.draw.rect(surface, boxColor, self.text_box)
        
        for row, line in enumerate(self.user_text):
            draw_text(line, font, self.rect.x, self.rect.y + (row * 18))
            
            self.text_box = pygame.Rect(self.rect.x+5,self.rect.y+(row * 18), 100, 30)
            

        
"""


        if self.cursor%4 == 0 and self.active:
            self.user_text = self.user_text + "|"
        self.cursor +=1

        
        try:
            if self.user_text[-1] == "|":
                  self.user_text = self.user_text[:-1]
        except:
            pass

        
        pygame.draw.rect(surface, 'light gray', self.rect, 0, 5)
        pygame.draw.rect(surface, 'black', self.rect, 2, 5)
        
        textSurface = font.render(self.user_text, True, 'black')

        

        self.text_box = pygame.Rect(self.rect.x+5,self.rect.y+5, 100, 30)
        self.text_box.w = (max(100, textSurface.get_width()+15))
        self.rect.w = (max(200, textSurface.get_width()+15))

        textBox = pygame.draw.rect(surface, boxColor, self.text_box)

        surface.blit(textSurface, (self.text_box.x+5, self.text_box.y+5))
"""

