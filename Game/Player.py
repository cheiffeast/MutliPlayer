from pygame import Rect

# CONSTANTS
WIDTH = 20
HEIGHT = 20

class player():
    def __init__(self, position, **kwargs):

        self.speed = kwargs.get("speed", 1)
        self.color = self.col = kwargs.get("color", [255, 255, 255])
        self.size  = kwargs.get("size", 20)

        self.position  = self.pos  = position
        self.rectangle = self.rect = Rect(self.position + [self.size, self.size])

        self.dx = 0
        self.dy = 0

    def move(self, rects, dx = 0, dy = 0):
        self.moveSingleAxis(rects, dx, 0)
        self.moveSingleAxis(rects, 0, dy)

        self.position = self.pos = [self.rect[0], self.rect[1]]

        return self.position


    def moveSingleAxis(self, rects, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        for rect in rects:
            if self.rect.colliderect(rect):
                if dx > 0:
                    self.rect.right = rect.left
                if dx < 0:
                    self.rect.left = rect.right
                if dy > 0:
                    self.rect.bottom = rect.top
                if dy < 0:
                    self.rect.top = rect.bottom
