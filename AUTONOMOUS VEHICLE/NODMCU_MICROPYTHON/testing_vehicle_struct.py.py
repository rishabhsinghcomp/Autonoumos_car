from machine import Pin
import time


def setup():
#     LEFT
    d3=	Pin(0, Pin.OUT)
    d4=	Pin(2, Pin.OUT)
    d3.off()
    d4.off()
#     RIGHT
    d5=	Pin(14, Pin.OUT)
    d6=	Pin(12, Pin.OUT)
    d5.off()
    d6.off()
    
    return [d3,d4,d5,d6]
    
    
    


def loop():
    d3,d4,d5,d6=setup()
    
    while(1):
        d3.on()
        d5.on()
        time.sleep(3)
        d3.off()
        d5.off()
        time.sleep(3)
        
        
        time.sleep(1)
        

loop()
        
        
        
    
    
    
    

