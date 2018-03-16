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


    def move(self, dx = 0, dy = 0):

        self.position[0] += dx * self.speed
        self.position[1] += dy * self.speed

        self.rectangle = self.rect = Rect(self.position + [self.size, self.size])

        return self.position


