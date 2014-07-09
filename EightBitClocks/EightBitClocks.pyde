"""
  Object Clock Example for 8bit Seminar (bit 6)
  Muthesius Kunsthochschule Sommersemester 2014
"""

# Hier sollen alle Uhren eingefügt werden
from JensClock import JensClock
from BenClock import BenClock

jensClock = JensClock()
bensClock = BenClock()

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
    translate(width/4, height/2)
    bensClock.draw()
    popMatrix()
