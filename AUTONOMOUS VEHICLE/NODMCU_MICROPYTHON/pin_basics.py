from machine import Pin

d0 = Pin(5, Pin.OUT)   #d0 
d0.off()                 


led_near_ant = Pin(2, Pin.OUT)   #also d4   #gpio2 is led near antenna and its inversed
led_near_ant.on()


# d2 = Pin(4,Pin. IN)
# d2 = Pin(4, Pin.OUT)
# d2.off()  




d3 = Pin(0, Pin.OUT)  #d3
d3.off()    