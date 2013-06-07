#!/usr/bin/env python2.7  

#Import delle Librerie
import RPi.GPIO as GPIO
import time

#definsco la numerazione dei pin
GPIO.setmode(GPIO.BOARD)

#definisco i channels dei  pin in input
channel1 = 3
channel2 = 5
channel3 = 7
channel4 = 11
channel5 = 13
channel6 = 15
channel7 = 19
channel8 = 21

#imposto i channels come input (pull down virtuale)
GPIO.setup(channel1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#definisco il numero di colonna
column = 0

#program header printed on the screen
try:
    print "Callback reading example for MickFenneck's HighSchool Final Project"
    print "GPIO IN:  3, 5, 7, 11, 13, 15, 19, 21\n"
    print "GPIO OUT: 8, 10, 12, 16, 18, 22, 24\n"
    raw_input("Premi Enter per far cominciare l'analisi...")

    #definisco la funzione di callback generale
    def callback1(channel):
        print 'riga: ', channel, ' colonna : ', column

    #event detect per i diversi canali (tempo di attesa 150 ms)
    GPIO.add_event_detect(channel1, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel2, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel3, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel4, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel5, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel6, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel7, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel8, GPIO.RISING, callback=callback1, bouncetime=150)
    
    print "The program will now start..."
    #numero dei pin in uscita
    pin_out = [8, 10, 12, 16, 18, 22, 24]
    #inizializzo i pin come uscite
    for ch_ext in pin_out:
        GPIO.setup(ch_ext, GPIO.OUT,initial=GPIO.LOW)
    #ciclo polling per cambiare pin in uscita
    while True:
        for ch_out in pin_out:
            column = ch_out
            GPIO.output(ch_out, GPIO.HIGH)
            time.sleep(0.025)     
            GPIO.output(ch_out, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
print "\n================================== the end ======================================"
