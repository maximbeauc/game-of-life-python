import pygame
import random
from button import Button

class GameOfLifeGUI:
    def __init__(self, board):
        BUTTON_BUFFER = 10
        BUTTON_HEIGHT = 30
        BUTTON_WIDTH = 80
        
        pygame.init()

        self.running = True
        self.playing = False
        self.board = board

        screen_info = pygame.display.Info()
        height = screen_info.current_h * 0.9 - (BUTTON_HEIGHT + BUTTON_BUFFER * 2)
        width = screen_info.current_w * 0.9
        self.size = min(height // self.board.rows, width // self.board.cols)

        self.screen = pygame.display.set_mode((self.board.cols * self.size, self.board.rows * self.size + 50))
        self.clock = pygame.time.Clock()

        self.clear = Button("Clear", (255, 255, 255), (BUTTON_BUFFER, height + BUTTON_BUFFER, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.random = Button("Random", (255, 255, 255), (BUTTON_BUFFER + BUTTON_WIDTH + BUTTON_BUFFER, height + BUTTON_BUFFER, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.start_stop = Button("Start/Stop", (255, 255, 255), (BUTTON_BUFFER + 2 * (BUTTON_WIDTH + BUTTON_BUFFER), height + BUTTON_BUFFER, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.step = Button("Step", (255, 255, 255), (BUTTON_BUFFER + 3 * (BUTTON_WIDTH + BUTTON_BUFFER), height + BUTTON_BUFFER, BUTTON_WIDTH, BUTTON_HEIGHT))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.playing = not self.playing

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_stop.is_clicked(event.pos):
                    self.playing = not self.playing
                elif self.playing:
                    return
                elif self.clear.is_clicked(event.pos) :
                    self.board.grid = [[0] * self.board.cols for _ in range(self.board.rows)]
                elif self.random.is_clicked(event.pos):
                    self.board.grid = [[random.choice([0, 1]) for _ in range(self.board.cols)] 
                                       for _ in range(self.board.rows)]
                elif self.step.is_clicked(event.pos):
                    self.board.update()
                else:            
                    mouseX, mouseY = pygame.mouse.get_pos()
                    col = (int)(mouseX / self.size)
                    row = (int)(mouseY / self.size)
                    if (0 <= row < self.board.rows and 0 <= col < self.board.cols):
                        self.board.grid[row][col] = not self.board.grid[row][col]
    
    def play(self):
        last_update_time = 0
        update_delay = 100

        while self.running:
            self.handle_events()
            if self.playing:
                current_time = pygame.time.get_ticks()
                if current_time - last_update_time > update_delay:
                    self.board.update()
                    last_update_time = current_time
            self.render()
            self.clock.tick(60)

    def render(self):
        self.screen.fill((0, 0, 0))

        for i in range(self.board.rows):
            for j in range(self.board.cols):
                if (self.board.grid[i][j]):
                    pygame.draw.rect(self.screen, (255, 255, 255), (j * self.size, i * self.size, self.size, self.size))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (j * self.size, i * self.size, self.size, self.size), 1)
        
        self.clear.draw(self.screen)
        self.random.draw(self.screen)  
        self.start_stop.draw(self.screen)
        self.step.draw(self.screen)

        pygame.display.flip()
                