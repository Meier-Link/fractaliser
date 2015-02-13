fractaliser
===========

A simple and funny script to use Turtle module to display fractal.

Dependencies
------------

Just python 3 (tested with python 3.2) and Turtle module.

Usage
-----

 * -h: display help
 * --iterations=<int>: Set how many time fractal will iterate to the recursive function
 * --intuple=<tuple>: Set input tuple formed as x1,y1,x2,y2,r,g,b
 * --modtuple=<tuple>: Modifications applied to the intuple

### Example

	./fractaliser.py --intuple=2.5,0.5,0.4,2,10,10,10 --modtuple='*1.0004,*1.0006,*1.0005,*1.0002,+2,+5,+10' --iterations=4000

Here we have 2 input points: (2.5,0.5), (0.4,2) and the value for red green blue (resp. 10,10,10).
The modtuple is formed following the same way as the intuple, plus a symbol ahead of each value.
In this example, the fractaliser will do 4000 iterations (and it's very long ... Almost an hour).

