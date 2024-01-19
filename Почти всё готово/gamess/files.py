import pygame


class Button1:
    def __init__(self, x, y, text, image_path=None, hover_images_path=None):
        self.x = x
        self.y = y
        self.width = 252
        self.height = 74
        self.text = text

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.hover_image = self.image
        if hover_images_path:
            self.hover_image = pygame.image.load(hover_images_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image.convert_alpha(screen), self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface.convert_alpha(screen), text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Button2:
    def __init__(self, x, y, text, image_path=None, hover_images_path=None):
        self.x = x
        self.y = y
        self.width = 252
        self.height = 74
        self.text = text

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.hover_image = self.image
        if hover_images_path:
            self.hover_image = pygame.image.load(hover_images_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image.convert_alpha(screen), self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface.convert_alpha(screen), text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Button3:
    def __init__(self, x, y, text, image_path=None, hover_images_path=None):
        self.x = x
        self.y = y
        self.width = 252
        self.height = 74
        self.text = text

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.hover_image = self.image
        if hover_images_path:
            self.hover_image = pygame.image.load(hover_images_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image.convert_alpha(screen), self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface.convert_alpha(screen), text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Button4:
    def __init__(self, x, y, text, image_path=None, hover_images_path=None):
        self.x = x
        self.y = y
        self.width = 252
        self.height = 74
        self.text = text

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.hover_image = self.image
        if hover_images_path:
            self.hover_image = pygame.image.load(hover_images_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image.convert_alpha(screen), self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface.convert_alpha(screen), text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Button5:
    def __init__(self, x, y, text, image_path=None, hover_images_path=None):
        self.x = x
        self.y = y
        self.width = 252
        self.height = 74
        self.text = text

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.hover_image = self.image
        if hover_images_path:
            self.hover_image = pygame.image.load(hover_images_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image.convert_alpha(screen), self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface.convert_alpha(screen), text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
