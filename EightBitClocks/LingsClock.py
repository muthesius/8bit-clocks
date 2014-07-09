class Runde:
    # Eigenschaften des Zeigers
    length=0
    weight=0
    red = 0
    green = 0
    blue = 0
    
    def update(): pass
    
    # Methoden des Zeigers
    def draw(self):
        self.update()
        pushMatrix()        
        strokeWeight(self.weight)
        stroke(self.red,self.green,self.blue, 100)
        strokeCap(ROUND)
        point(self.length, 0)
        popMatrix()
    
class SekundenRunde(Runde):
    red=255
    length=100
    
    
    def update(self):       
        self.weight=map(second(),0,59,0,320)
        
class MinutenRunde(Runde):
    green=255
    blue=255
    
    
    def update(self):   
        self.weight=map(minute(),0,59,0,320)
        
class StundenRunde(Runde):
    red=127
    blue=255    
    length=-100
    
    
    def update(self):
        self.weight=map(hour(),0,59,0,320)
    
    

        
class LingClock:
    sekunden=SekundenRunde()
    minuten=MinutenRunde()
    stunden=StundenRunde()
   
    
    def draw(self):
        self.sekunden.draw()
        self.minuten.draw()
        self.stunden.draw()
       
