"""
  Object Clock Example for 8bit Seminar (bit 6)
  Muthesius Kunsthochschule Sommersemester 2014
"""

# Hier sollen alle Uhren eingefügt werden
from JensClock import JensClock
from HermannClock import HermannClock

jensClock = JensClock()
HermannClock = HermannClock()

def setup():
    size(640,320)

def draw():
    smooth()
    background(255)

    # Hier als Beispiel die Uhr zum Zeichnen einfügen
    pushMatrix()
    translate(width/2, height/2)
    jensClock.draw()
    popMatrix()
    
    pushMatrix()
    translate(width/5, height/2)
    HermannClock.draw()
    popMatrix()

