from settings import *

class Timer: # Timer setup from the tutorial
    def __init__(self, duration, function, auto_start):
        self.active = False
        self.start_time = 0
        self.duration = duration
        self.func = function

        if auto_start: self.start()
        

    def __bool__(self): # method returned when putting the object in a condition
        return self.active

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.active = True
    
    def stop(self):
        self.start_time = 0
        self.active = False

    def update(self):
        if self.active:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.duration:
                if self.func and self.start_time != 0: self.func() # prevent calling func at the start
                self.stop()