from turtle import *

speed(0)  # For the highest speed, use `0` instead of `250`.
color('cyan')
bgcolor('black')

b = 1

while b <= 350:
    left(b)
    forward(b * 1)
    b += 1  

done() 
