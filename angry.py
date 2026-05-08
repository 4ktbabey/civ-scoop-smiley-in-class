import time
from smiley import Smiley
from blinkable import Blinkable

class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(self.RED)

        self.draw_brows()
        self.draw_mouth()
        self.draw_eyes()
        

    def draw_brows(self):
        '''
        Draws the mouth
        '''
        brows = [8, 9, 18, 21, 14, 15]
        for pixel in brows:
            self.pixels[pixel] = self.WHITE

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 42, 43, 44, 45, 54]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [17, 25, 30, 22]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion
            self.pixels[pixel] = eyes

    def blink(self, delay=0.25):
        """
       Blinks the smiley's eyes once
        
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()

