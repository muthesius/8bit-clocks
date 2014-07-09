from LingClock import *

clock=LingClock()


def setup():
    size(320,320)
      
def draw():
    smooth()
    background(255)
    
    translate(width/2, height/2)    
    clock.draw()
    
    
    
     
   
