import pygame

def events(gamefield):
    done = False
    gaming_loop = True

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                gamefield.set_live(x_mouse, y_mouse)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gaming_loop = False if gaming_loop == True else True

                if event.key == pygame.K_ESCAPE:
                    gamefield.set_default()

                if event.key == pygame.K_r:
                    if gamefield.random_flag:
                        gamefield.set_default()
                        gamefield.set_random(gamefield.per_cover, gamefield.per_fill)

        if not gaming_loop:

            gamefield.counting_cells()
            gamefield.cell_selection()

            gamefield.game_speed_tick()

        pygame.display.update()
