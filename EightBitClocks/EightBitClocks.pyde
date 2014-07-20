"""
  Object Clock Example for 8bit Seminar (bit 6)
  Muthesius Kunsthochschule Sommersemester 2014
"""

# Hier sollen alle Uhren eingefügt werden
from JensClock import JensClock
from HermannClock import HermannClock
from BenClock import BenClock
from FeiClock import FeiClock
from LingClock import LingClock


jensClock = JensClock()
hermannClock = HermannClock()
benClock = BenClock()
lingClock = LingClock()
feiClock = FeiClock()

def setup():
    size(800,800)

def draw():
    smooth()
    background(255)

    # Hier als Beispiel die Uhr zum Zeichnen einfügen

    pushMatrix()
    translate(width/6, height/4)
    jensClock.draw()
    popMatrix()

    pushMatrix()
    translate(3 * width/6, height/4)
    hermannClock.draw()
    popMatrix()

    pushMatrix()
    translate(5 * width/6, height/4)
    benClock.draw()
    popMatrix()

    pushMatrix()
    translate(width/6, 3 * height/4)
    lingClock.draw()
    popMatrix()

    pushMatrix()
    translate(3 * width/6, 3 * height/4)
    feiClock.draw()
    popMatrix()

