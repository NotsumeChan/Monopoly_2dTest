import pygame as p
import sys as s
from threading import *
p.init()

def main():
    #definir colores
    global BLANCO
    BLANCO = (255,255,255)
    global NEGRO 
    NEGRO = (0,0,0)
    
    #variables
    
    size = [600,400]
    
    Screen = p.display.set_mode(size)
    p.time.Clock().tick(30) #fps



    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                s.exit()
            print(event)
        

        
if __name__ == '__main__':
    main()