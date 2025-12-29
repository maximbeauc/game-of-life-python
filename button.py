import pygame

class Button:
    def __init__(self, text = "", color = (255, 255, 255), pos = (0, 0, 50, 50)):
        self.text = text
        self.color = color
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.w = pos[2]
        self.h = pos[3]
        self.font = pygame.font.Font(None, 16)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.pos)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        screen.blit(text_surface, text_rect)

    
    def is_clicked(self, mouse_pos):
        return (self.x < mouse_pos[0] < self.x + self.w 
                and self.y < mouse_pos[1] < self.y + self.h)
    
    def set_position(self, pos):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.w = pos[2]
        self.h = pos[3]
    
    def set_text(self, text):
        self.text = text
    
    def set_colour(self, colour):
        self.color = colour