from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

P = yellow
O = nothing


def dot():
    digit = [
    O,
    O,
    O,
    P,
    ]
    return digit
def one():
    digit = [
    P,
    P,
    P,
    P,
    ]
    return digit
def two():
    digit = [
    P, P, P,
    O, P, P,
    P, O, O,
    P, P, P,
    ]
    return digit
def three():
    digit = [
    P, P, P,
    O, P, P,
    O, O, P,
    P, P, P,
    ]
    return digit
def four():
    digit = [
    P, O, P,
    P, P, P,
    O, O, P,
    O, O, P,
    ]
    return digit
def five():
    digit = [
    P, P, P,
    P, P, O,
    O, O, P,
    P, P, P,
    ]
    return digit
def six():
    digit = [
    O, P, P,
    P, O, O,
    P, P, P,
    P, P, P,
    ]
    return digit
def seven():
    digit = [
    P, P, P,
    O, P, P,
    P, O, O,
    P, O, O,
    ]
    return digit
def eight():
    digit = [
    P, P, P,
    P, O, P,
    P, P, P,
    P, P, P,
    ]
    return digit
def nine():
    digit = [
    P, P, P,
    P, O, P,
    P, P, P,
    O, O, P,
    ]
    return digit
def zero():
    digit = [
    P, P, P,
    P, O, P,
    P, O, P,
    P, P, P,
    ]
    return digit

    
charmap = {
  '1' : one(),
  '2' : two(),
  '3' : three(),
  '4' : four(),
  '5' : five(),
  '6' : six(),
  '7' : seven(),
  '8' : eight(),
  '9' : nine(),
  '0' : zero(),
  '.' : dot()
}


def renderChar(pos, char):
  w = len(char) // 4
  for x in range(0, w):
    for y in range(0, 4):
      xscreen = pos + x
      if (xscreen >= 0 and xscreen < 8):
        s.set_pixel(xscreen, y, char[w * y + x])
  return w + 1

def render(text):
  charpos = textpos = 7
  while charpos > 0:
    s.clear()
    charpos = textpos
    for c in text:
      charpos += renderChar(charpos, charmap[c])
    #print charpos
    time.sleep(0.15)
    textpos -= 1

while True: 
  render("192.168.1.41")

