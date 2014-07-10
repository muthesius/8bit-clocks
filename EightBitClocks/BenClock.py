"""
Displays a clock in local time

Time may be modified by optional offset parameter to Clock
constructor (in hours), e.g. BenClock(-1) 
"""

class Hand:
    maxLength = 60
    strokeWeight = 20
    red = 0
    green = 0
    blue = 0
    
    def __init__(self):
        # make shure there is always a set length for any instance/subclass
        self.length = 20

    def draw(self):
        self.update()
        strokeWeight(self.strokeWeight)
        stroke(self.red, self.green, self.blue)
        line(0, 0, self.length, 0)
    
    def update(self):
        pass

class SecondsHand(Hand):
    red = 255
    green = 255
    
    def update(self):
        translate(0, 2 * self.strokeWeight)
        self.length = map(second(), 0, 60, 0, self.maxLength)

class MinutesHand(Hand):
    red = 255
    
    def update(self):
        self.length = map(minute(), 0, 60, 0, self.maxLength)

class HoursHand(Hand):
    def __init__(self, offset = 0):
        # First of all, call parent constructor cause we're overriding it here
        Hand.__init__(self)
        self.offset = offset
        
    def update(self):
        translate(0, -1 * self.strokeWeight)
        self.length = map(hour() + self.offset, 0, 12, 0, self.maxLength)

class BenClock:
    def __init__(self, offset = 0):
        self.offset = offset
        self.secondsHand = SecondsHand()
        self.minutesHand = MinutesHand()
        self.hoursHand = HoursHand(self.offset)

    def draw(self): # TODO Translate() here, make x/y optional arguments
        self.minutesHand.draw()
        self.hoursHand.draw()
        self.secondsHand.draw()
