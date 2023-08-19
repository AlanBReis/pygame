import pygame

pygame.init()

s_width = 576
s_height = 324

print("Set Start")
# Criação de janela do pygame
screen = pygame.display.set_mode(size=(s_width, s_height))

# Carregar imagem e gerar superficie
bg_surface = pygame.image.load("./asset/background.png").convert_alpha()
player1_surf = pygame.image.load("./asset/player1.png").convert_alpha()

# Obter o retangulo da superficie
bg_rect: Rect = bg_surface.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=0, top=0)

# Desenhar na janela (screen)
screen.blit(source=bg_surface, dest=(bg_rect))
screen.blit(source=player1_surf, dest=(player1_rect))

# Atualizar a janela
pygame.display.flip()

print("Set End")
print("Loop Start")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("loop end")
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key(pygame.K_w):
        pass
