#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   fractal.py
#
#   A script who display a fractal based on a tuple.
#
#   This program is free software licensed under the Creative Commons
#   Attribution-NonCommercial-ShareAlike 3.0 France License.
#   To view a copy of this license, visit 
#   http://creativecommons.org/licenses/by-nc-sa/3.0/fr/
#   or send a letter to Creative Commons, 
#   444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

from random import randint
from time import sleep, time
import turtle as t
import math as m
import getopt
import sys

__version__ = "0.1"
__author__ = "Jérémie Balagna-Ranin <jeremie.balagna@gmail.com>"


class Fractal(object):
  '''Main fractal class'''
  
  def __init__(self, intuple, modtuple):
    '''Initialisation of fractal object'''
    self.ADD = 0
    self.SUB = 1
    self.MUL = 2
    self.DIV = 3
    self.POW = 4
    self.MOD = 5
    
    self.data = []
    for value in intuple:
      self.data.append(float(value))
    self.data = tuple(self.data)
    self.manips = list(self.data)
    
    self.mod = []
    for mod in modtuple:
        if mod[0] == '+':
          self.mod.append((self.ADD, float(mod[1:])))
        elif mod[0] == '-':
          self.mod.append((self.SUB, float(mod[1:])))
        elif mod[0] == '*':
          self.mod.append((self.MUL, float(mod[1:])))
        elif mod[0] == '/':
          self.mod.append((self.DIV, float(mod[1:])))
        elif mod[0] == '%':
          self.mod.append((self.MOD, float(mod[1:])))
        else:
          self.mod.append((self.ADD, float(mod)))
  
  def calculate(self):
    '''Do the operation'''
    for i in range(0, len(self.mod)):
      if self.mod[i][0] == self.ADD:
        self.manips[i] += self.mod[i][1]
      elif self.mod[i][0] == self.SUB:
        self.manips[i] -= self.mod[i][1]
      elif self.mod[i][0] == self.MUL:
        self.manips[i] *= self.mod[i][1]
      elif self.mod[i][0] == self.DIV:
        self.manips[i] /= self.mod[i][1]
      elif self.mod[i][0] == self.POW:
        self.manips[i] **= self.mod[i][1]
      elif self.mod[i][0] == self.MOD:
        self.manips[i] %= self.mod[i][1]
    print(self.manips)

  def get(self):
    '''Simply return the working tuple'''
    return self.manips
    

def dtan(fr, to):
  '''directly return angle in degreeses and dist to trace from two points'''
  dx = to[0] - fr[0]
  dy = to[1] - fr[1]
  if dy == 0:
    dy = 1
  hyp = int(m.sqrt(dx**2 + dy**2))
  ang = int(m.degrees(m.tan(dx / dy)))
  return (ang, hyp)

def usage():
  print('''Usage: ./fractaliser.py [options]''')
  print(''' -h:                 print this help and exit''')
  print(''' --iterations=<int>: set how many time fractal will iterate to the''')
  print('''                     recursive function''')
  print(''' --intuple=<tuple>:  set input tuple formed as x1,y1,x2,y2,...''')
  print('''                     Here, tuple may has the following form:''')
  print('''                     x1,y1,x2,y2,r,g,b''')
  print('''                     where x1,y1: coord of first point''')
  print('''                     where x2,y2: coord of second point''')
  print('''                     where r,g,b: composants of color''')
  print(''' --modtuple=<tuple>: set modificator tuple formed as ''')
  print('''                     <symbol>x1,<symbol>y1,<symbol>x2,...''')
  print('''                     Here, tuple may has the following form:''')
  print('''                     x1,y1,x2,y2,r,g,b''')
  print('''                     with symbole ahead of value''')

def draw(img):
  ang, hyp = dtan((img[0], img[1]), (img[2], img[3]))
  t.color(img[4] % 255, img[5] % 255, img[6] % 255)
  t.left(ang)
  t.forward(hyp)

def run(intuple, modtuple, ite=42):
  # init turtle screen
  t.title("Simple fractal try")
  t.hideturtle()
  t.colormode(255)
  t.color(255, 255, 255)
  
  # Start display
  print('''Start render''')
  stime = int(time())
  fractal = Fractal(intuple, modtuple)
  draw(fractal.get())
  for i in range(1, ite):
    fractal.calculate()
    draw(fractal.get())
    sleep(0.1)
    if i % 10 == 0:
      print('''-------------------- ''' + str(i) + ''' iterations --------------------''')
      sleep(0.1)
    if i % 100 == 0:
      sleep(0.5)
  etime = int(time())
  diff_t = etime - stime
  diff_m = int(diff_t / 60)
  diff_s = int(diff_t % 60)
  print('''Finish render in ''', diff_m, ''' min and ''', diff_s, ''' sec.''')
  t.exitonclick()

if __name__ == '__main__':
  # Args management
  try:
    opts, args = getopt.getopt(sys.argv[1:], "h", 
                              ["iterations=", "intuple=", "modtuple=", "help"])
  except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(1)
  
  ite = 42
  intuple = ('0', '0', '42', '42', '0', '0', '0')
  modtuple = ('+42', '+42', '+42', '+42', '+42', '+42', '+42')

  for o, a in opts:
    if o in('-h', '--help'):
      usage()
      sys.exit()
      continue
    if o == '--iterations':
      ite = int(a)
      continue
    if o == '--intuple':
      intuple = tuple(a.split(','))
      if len(intuple) != 7:
        print('''intuple must be with 7 values separated by ',' ''')
      continue
    if o == '--modtuple':
      modtuple = tuple(a.split(','))
      if len(modtuple) != 7:
        print('''modtuple must be with 7 values separated by ',' ''')
      continue
  
  run(intuple, modtuple, ite)

