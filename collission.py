import pygame as pg 
import numpy as np 
from pgquadtree import point, cell, quad_tree


class particle:
    def __init__(self, radius=4, pos=[0, 0]):
        self.r = radius
        self.x = pos[0]
        self.y = pos[1]
        self.v = None

    def update(self):
        self.v = np.random.randint(-5, 6, 2)
        self.x    += self.v[0]
        self.y    += self.v[1]

    def draw(self, surf, clr=(55, 55, 255)):
        pg.draw.circle(surf, clr, (self.x, self.y), self.r, 0)




if __name__ == '__main__':


    rds       = 20
    particles = [particle(rds, np.random.randint(0, 800, 2)) for i in range(10)]
    bdry      = cell(400, 400, 400, 400)
    qtree     = quad_tree(bdry)

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
            p.update()
            p.draw(surf, (0, 0, 255))
            if p.x < 800 and p.y < 800:
                qtree.insert(point(p.x, p.y, p))
        for p in particles:
            c = cell(p.x, p.y, rds, rds)
            c.draw(surf, (0, 255, 0))
            fnd = qtree.query(c)
            # print(p.x, p.y, c.x, c.y, c.half_width)
            if len(fnd):
                print(fnd[0].userdata.x)
            for pt in fnd:
                # print(pt.userdata.x)
                if pt.userdata.x != p.x or pt.userdata.y != p.y:
                    pt.userdata.draw(surf, (255, 0, 0))
        # print("new\n")


        screen.blit(surf, position)
        
        cur_fps = font.render(str(int(clock.get_fps())), False, (255, 0, 0))
        screen.blit(cur_fps, (10, 10))
        pg.display.update()
        clock.tick(144)

