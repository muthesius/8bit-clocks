"""
  Object Clock Example for 8bit Seminar (bit 6)
  Muthesius Kunsthochschule Sommersemester 2014
"""

# Hier sollen alle Uhren eingefügt werden
from JensClock import JensClock

clockJens = JensClock()


def setup():
    size(640,320)

def draw():
    smooth()
    background(255)

    # Hier als Beispiel die Uhr zum Zeichnen einfügen
    clockJens.draw(width * 1/4.0, height/2)

