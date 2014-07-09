class Zeiger:
    # Eigenschaften des Zeigers
    length = 100
    rotation = 0
    red = 0
    green = 0
    blue = 0
    
    redFill = 0
    greenFill = 0
    blueFill = 0

    thick1= 15
    thick2 = thick1 * -1
    
    def update(self): pass
    
    # Methoden des Zeigers
    def draw(self):
        self.update()
        pushMatrix()
        rotate(self.rotation - HALF_PI)
        fill(self.redFill, self.greenFill, self.blueFill)
        strokeWeight(5)
        triangle(self.thick1, 0 ,self.thick2, 0,0,self.length)
        popMatrix()
    
class SekundenZeiger(Zeiger):
    length = 100
    red = 0
    green = 0
    blue = 0
    
    redFill = 255
    greenFill = 0
    blueFill = 0
    
    def update(self):
        self.rotation = map(second(), 0, 59, 0, TWO_PI)
        
    

class MinutenZeiger(Zeiger):


    redFill = 255
    greenFill = 255
    blueFill = 0

    
    def update(self):
        self.rotation = map(minute() + second()/59.0, 0, 59, 0, TWO_PI)
        
class StundenZeiger(Zeiger):
    length = 70
    
    redFill = 60
    greenFill = 60
    blueFill = 60

    
    def update(self):
        self.rotation = map(hour()+ minute()/59.0, 0, 12, 0, TWO_PI)
 
        
class ZiffernBlatt:
    
    red = 0
    green = 0
    blue = 0
    
    
    def draw(self):
        for x in range(0,12):
        
            pushMatrix()
            rotate(map(x,0,12,0,TWO_PI))
            strokeWeight(10)
            point(15,100)
            
            popMatrix()

    
        
            
                    
                             

class HermannClock:
    sekunden = SekundenZeiger()
    minuten  = MinutenZeiger()
    stunden  = StundenZeiger()
    Ziffernblatt = ZiffernBlatt()
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
        self.Ziffernblatt.draw()
        popMatrix()
        popMatrix()

