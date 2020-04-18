import pygame as pg 

class point:
    def __init__(self, x, y, data=None):
        self.x        = x
        self.y        = y
        self.userdata = data

    def draw(self, surf, clr=[255, 55, 0]):
        pg.draw.circle(surf, clr, (self.x, self.y), 2, 0)

class cell:
    def __init__(self, x, y, half_width, half_height):
        self.x  = x
        self.y  = y
        self.half_width = half_width
        self.half_height = half_height

        self.min_x = self.x - self.half_width
        self.max_x = self.x + self.half_width
        self.min_y = self.y - self.half_height
        self.max_y = self.y + self.half_height


    def contains(self, pt):
        x, y = pt.x, pt.y

        if x <= self.max_x and x >= self.min_x and y <= self.max_y and y >= self.min_y:
            return True

        return False 


    def intersect(self, cel):
        if (self.min_x > cel.max_x or cel.min_x > self.max_x) or (
                 self.min_y > cel.max_y or cel.min_y > self.max_y):
            return False

        return True

    def draw(self, surf, clr=[255, 255, 0]):
        pg.draw.rect(surf, clr, (self.min_x, self.min_y, 2 * self.half_width, 2 * self.half_height), 1)


class quad_tree:
    hgt = 1
    def __init__(self, cell, cap=4, lvl=0):
        self.boundary = cell 
        self.capacity = cap
        self.points   = []
        self.divided  = False

        self.n_points = 0
        self.level    = lvl

        if self.level + 1 > quad_tree.hgt:
            quad_tree.hgt = self.level + 1


    def subdivide(self):
        new_w = self.boundary.half_width / 2
        new_h = self.boundary.half_height / 2
       
        x = self.boundary.x
        y = self.boundary.y

        self.divided = True
        
        self.ne = quad_tree(cell(x+new_w, y+new_h, new_w, new_h), self.capacity, self.level+1)
        self.nw = quad_tree(cell(x-new_w, y+new_h, new_w, new_h), self.capacity, self.level+1)
        self.se = quad_tree(cell(x+new_w, y-new_h, new_w, new_h), self.capacity, self.level+1)
        self.sw = quad_tree(cell(x-new_w, y-new_h, new_w, new_h), self.capacity, self.level+1)

    def insert(self, pt):   
        if not self.boundary.contains(pt):
            return False

        self.n_points += 1

        if (len(self.points) < self.capacity):
            self.points.append(pt)
            return True

        if not self.divided:
            self.subdivide()


        if (self.nw.insert(pt)): return True
        if (self.ne.insert(pt)): return True
        if (self.sw.insert(pt)): return True
        if (self.se.insert(pt)): return True

        return False

    def query(self, range):
        found = []
        if not self.boundary.intersect(range):
            return found

        for pt in self.points:
            if range.contains(pt):
                found.append(pt)

        if self.divided:
            found.extend(self.ne.query(range))
            found.extend(self.nw.query(range))
            found.extend(self.se.query(range))
            found.extend(self.sw.query(range))

        return found





    def draw(self, surf):
        self.boundary.draw(surf)

        for pt in self.points:
            pt.draw(surf)

        if self.divided:
            self.ne.draw(surf)
            self.nw.draw(surf)
            self.se.draw(surf)
            self.sw.draw(surf)



################################ EXAMPLE ########################################
# initialzation
# c  = cell(400, 400, 400, 400)
# qt = quad_tree(c, 4)
#
# insert function
# qt.insert(point(100, 200)) 
#     
# query function
# qrcell = cell(100, 50, 100, 300)
# fnd    = qt.query(qrcell)
#
############################ ################### ################################