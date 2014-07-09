"""
  Object Clock Example for 8bit Seminar (bit 6)
  Muthesius Kunsthochschule Sommersemester 2014
"""

from JensClock import JensClock

clockBerlin = JensClock()
clockLondon = JensClock(-1)

def setup():
    size(640,320)

def draw():
    smooth()
    background(255)

    clockBerlin.draw(width * 1/4.0, height/2)

    clockLondon.draw(width * 3/4.0, height/2)

