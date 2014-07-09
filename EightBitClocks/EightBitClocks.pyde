"""
  Object Clock Example for 8bit Seminar (bit 6)
  Muthesius Kunsthochschule Sommersemester 2014
"""

# Hier sollen alle Uhren eingefügt werden
from JensClock import JensClock
from BenClock import BenClock

clockJens = JensClock()
clockBen = BenClock()


def setup():
    size(640,320)

def draw():
    smooth()
    background(255)

    # Hier als Beispiel die Uhr zum Zeichnen einfügen
    translate(width * 1/4.0, height/2)
    clockJens.draw()
    translate(width * 2/4.0, 0)
    clockBen.draw()

