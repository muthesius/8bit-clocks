

# Hier sollen alle Uhren eingefügt werden
from JensClock import JensClock
from HermannClock import HermannClock
from BenClock import BenClock
from LingClock import *


jensClock = JensClock()
HermannClock = HermannClock()
bensClock = BenClock()

clock=LingsClock()


def setup():
    size(320,320)

def draw():
    smooth()
    background(255)


    translate(width/2, height/2)
    clock.draw()


    # Hier als Beispiel die Uhr zum Zeichnen einfügen
    pushMatrix()
    translate(width/2, height/2)
    jensClock.draw()
    popMatrix()

<<<<<<< HEAD

=======
>>>>>>> master
    pushMatrix()
    translate(width/5, height/2)
    HermannClock.draw()
    popMatrix()

<<<<<<< HEAD

=======
>>>>>>> master
    pushMatrix()
    translate(width/4, height/2)
    bensClock.draw()
    popMatrix()
<<<<<<< HEAD

=======
>>>>>>> master
