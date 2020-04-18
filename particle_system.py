import pygame as pg 
import numpy as np 


class particle:
    def __init__(self, radius=4, pos=[0, 0], velocity=[0, 0], acc=[0, 0]):
        self.r = radius
        self.x = pos[0]
        self.y = pos[1]
        self.v = velocity
        self.a = acc 

    def update(self):
        self.v = np.random.randint(-5, 6, 2)
        # self.a = 
        self.x    += self.v[0]
        self.y    += self.v[1]
        # self.v[0] += self.a[0]
        # self.v[1] += self.a[1]

    def draw(self, surf):
        pg.draw.circle(surf, (55, 55, 255), (self.x, self.y), self.r, 0)



if __name__ == '__main__':


    particles = [particle(7, np.random.randint(0, 800, 2), np.random.randint(-1, 2, 2), [0, 0]) for i in range(1000)]

    pg.init()

    screen_size = (1540, 800)
    bg          = (0, 0, 0)
    wt          = (255, 255, 255)
    position    = (400, 0)
    surf        = pg.Surface((800, 800))
    rect        = surf.get_rect(topleft=position)

    font_size = 15
    font = pg.font.SysFont("Segoe Print", font_size)

    screen = pg.display.set_mode(screen_size)
    pg.display.set_caption('particle system')
    clock = pg.time.Clock()
  
    surf.fill(wt)

    crash       = True
    while crash:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crash = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    crash = False


        screen.fill(bg)
        surf.fill(wt)

        for p in particles:
            p.draw(surf)
            p.update()


        screen.blit(surf, position)
        
        cur_fps = font.render(str(int(clock.get_fps())), False, (255, 0, 0))
        screen.blit(cur_fps, (10, 10))
        pg.display.update()
        clock.tick(60)
