class Zeiger:
    # Eigenschaften des Zeigers
    length = 100
    rotation = 0
    red = 0
    green = 0
    blue = 0
    
    def update(self): pass
    
    # Methoden des Zeigers
    def draw(self):
        self.update()
        pushMatrix()
        rotate(self.rotation - HALF_PI)
        strokeWeight(1)
        stroke(self.red,self.green,self.blue, 127)
        line(0, 0, self.length, 0)
        popMatrix()
    
class SekundenZeiger(Zeiger):
    length = 120
    red = 127
    green = 127
    
    def update(self):
        self.rotation = map(second(), 0, 59, 0, TWO_PI)
        
    def draw(self):
        self.update()
        pushMatrix()
        rotate(self.rotation - HALF_PI)
        strokeWeight(15)
        stroke(self.red,self.green,self.blue, 127)
        strokeCap(ROUND)
        point(self.length, 0)
        popMatrix()

class MinutenZeiger(Zeiger):
    blue = 255
    green = 127
    
    def update(self):
        self.rotation = map(minute() + second()/59.0, 0, 59, 0, TWO_PI)
        
class StundenZeiger(Zeiger):
    length = 60
    red = 127
    green = 127
    
    def update(self):
        self.rotation = map(hour()+ minute()/59.0, 0, 12, 0, TWO_PI)
        

class JensClock:
    sekunden = SekundenZeiger()
    minuten  = MinutenZeiger()
    stunden  = StundenZeiger()
    offset = 0
    
    def __init__(self, offset = 0):
        self.offset = offset
    
    def draw(self, x = 0, y = 0):
        pushMatrix()
        translate(x,y)    
        self.sekunden.draw()
        self.minuten.draw()
        pushMatrix()
        rotate(self.offset * TWO_PI/12.0)
        self.stunden.draw()
        popMatrix()
        popMatrix()

