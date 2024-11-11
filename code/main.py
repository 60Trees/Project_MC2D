import pygame

# -----WINDOW CLASS-----
class Window:
    def __init__(self) -> None:
        self.width = 100
        self.height = 100
        self.size = self.width, self.height
        self.WIN = pygame.display.set_mode(100, 100, pygame.RESIZABLE)
window = Window()

# -----INPUT CLASS-----
class Input:
    def __init__(self) -> None:
        class Keyboard:
            def __init__(self) -> None:
                self.isPushed = pygame.key.get_pressed()
                self.isTyped = pygame.key.get_pressed()
        class Mouse:
            def __init__(self) -> None:
                self.mouse = pygame.mouse.get_pressed
                self.left = self.mouse[0]
                self.middle = self.mouse[1]
                self.right = self.mouse[2]
        self.keyboard = Keyboard()
        self.mouse = Mouse()
    def update(self, event):
        pass
input = Input()
# -----GAME CLASS-----
class Game:
    def __init__(self) -> None:
        self.done = False
game = Game()