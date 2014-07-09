

# Hier sollen alle Uhren eingefügt werden
from JensClock import JensClock
from HermannClock import HermannClock
from BenClock import BenClock

# @ling: hm... better filenameing...?
from LingsClock import LingClock


jensClock = JensClock()
HermannClock = HermannClock()
bensClock = BenClock()

lingsClock = LingClock()


def setup():
    size(320,320)

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

    pushMatrix()
    translate(width/4, height/2)
    bensClock.draw()
    popMatrix()

    translate(width/2, height/2)
    lingsClock.draw()

