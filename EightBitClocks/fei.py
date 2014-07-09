class Zeiger:
   length = 120
   rotation=0
   red=0
   green=0
   blue=0
  
   def update(self):pass
   
   def draw(self):
       self.update()
       pushMatrix()
       rotate(self.rotation - HALF_PI)
       strokeWeight(1)
       stroke(self.red, self.green, self.blue,127)
       
       line(0,0,self.length,0)

       popMatrix()
       

       
       
class SekundenZeiger(Zeiger):

    
    def update(self):
        self.rotation = map(second(),0,59,0,TWO_PI)
        
    def draw(self):
        self.update()
        pushMatrix()
        rotate(self.rotation - HALF_PI)
        strokeWeight(5)
        stroke(self.red, self.green, self.blue,127)
        
        point(self.length,0)

        popMatrix()
        
class MinutenZeiger(Zeiger):
    length=120
    red=0
    green=127
    
    
    def update(self):
        # wie kann ich den minutenzeiger etwas schneller laufen lassen?
        self.rotation= map(minute(),-108,59,0,TWO_PI)
        
class StundenZeiger(Zeiger):
    red=125

    
    
    def update(self):
        self.rotation= map(hour(),0,12,0,TWO_PI)
        
    def draw(self):
        self.update()
        pushMatrix()
        rotate(self.rotation - HALF_PI)
        strokeWeight(25)
        stroke(self.red, self.green, self.blue,127)
        
        point(self.length,0)


        popMatrix()
class Zeiger:
   sekunden= SekundenZeiger()
   minuten= MinutenZeiger()
   stunden=StundenZeiger()
   
   def draw(self):
        self.sekunden.draw()
        self.minuten.draw()
        self.stunden.draw()
