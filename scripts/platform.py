from scripts.sprite import Sprite
from scripts.constants import display_size
class Platform(Sprite):
    type = 'Platform'
    def update(self):
        pass

class MovingPlatform(Platform):
    type = 'MovingPlatform'
    def __init__(self, center, image, speed):
        super().__init__(center, image)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.speed = abs(self.speed)
        elif self.rect.right > display_size[0]:
            self.speed = -abs(self.speed)

class DisappearingPlatform(Platform):
    type = 'DisappearingPlatform'
    def __init__(self, center, image, disappearing_time):
        super().__init__(center, image)
        self.player_touched = False
        self.disappearing_start_time = disappearing_time
        self.disappearing_time = disappearing_time
    def update(self):
        if self.player_touched:
            self.disappearing_time -= 1
            mult = self.disappearing_time/ self.disappearing_start_time
            self.image.set_alpha(int(255*mult))
class BreakingPlatform(Platform):
    type = 'BreakingPlatform'
