#!/usr/bin/env python2.7  

# VERSIONE CON
# Pull down - tastopin8-pin10 pin/3.3v
# Con uso delle Callback

import time
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BOARD)  
      
pin8 = 8;
pin10 = 10;

# Pins come ingresso. Pulldown integrato  
GPIO.setup(pin8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
GPIO.setup(pin10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

print "Connetti un pulsante tra pin8 o pin10 e 3.3v\n" 
print "(configurazione pull DOWN con tasto verso 3.3v)\n"
raw_input("Premi invio quando sei pronto.... \n>")  

def callback_pin8(pin8):
    print "Qui scateno l'evento per il pin 8..."

def callback_pin10(pin10):
    print "Qui scateno l'evento per il pin 10..."

# Loop principale di attesa del tasto
try:
    print "Aspetto la pressione dei tasti..."
    GPIO.add_event_detect(pin8, GPIO.RISING, callback=callback_pin8, bouncetime=150)
    GPIO.add_event_detect(pin10, GPIO.RISING, callback=callback_pin10, bouncetime=150)

    while True:
        time.sleep(100)
      
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
