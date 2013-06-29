#!/usr/bin/env python2.7  

#Import delle Librerie
import RPi.GPIO as GPIO
import time
from Nsound import *
#from Nsound import use

#definisco l'audio PlayBack di libao
use("libao")

#definsco la numerazione dei pin
GPIO.setmode(GPIO.BOARD)

#definisco i channels dei  pin in input
channel1 = 7
channel2 = 11
channel3 = 13
channel4 = 15
channel5 = 19
channel6 = 21
channel7 = 23
channel8 = 26

#Matrice contenente le frequenze dei vari suoni
matrix = [
[   98,  156, 247, 392, 622, 988,0],     
[   93,  147, 233, 370, 587, 932,0],  
[   88,  139, 220, 349, 554, 880,0],    
[   83,  131, 208, 330, 523, 831,0],    
[   78,  124, 196, 311, 494, 784,0],   
[   74,  117, 158, 294, 466, 740,0],    
[   70,  110, 175, 277, 440, 698,0],  
[   66,  104, 165, 262, 415, 659, 1046]]


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
    #definisco la frequenza a cazzo
    sr = 22050.0
    #def. la sinusoide
    sine = Sine(sr)
    #definisco il suono
    suono = sine.generate(0.2,440.0)
    #definisco il playback 
    pb = AudioPlayback(sr, 1, 16)

    print "Callback reading example for MickFenneck's HighSchool Final Project"
    print "GPIO IN:  7, 11, 13, 15, 19, 21, 23, 28\n"
    print "GPIO OUT: 8, 10, 12, 16, 18, 22, 24\n"
    raw_input("Premi Enter per far cominciare l'analisi...")


    #calcola l' indice j della matrice RxC
    def columns(channel):
        if channel == 8:
            return 0
        elif channel == 10:
            return 1
        elif channel == 12:
            return 2
        elif channel == 16:
            return 3
        elif channel == 18:
            return 4
        elif channel == 22:
            return 5
        elif channel == 24:
            return 6
        else:
            return -1
        
    #calcola l' indice i della matrice RxC
    def rows(channel):
        if channel == 7:
            return 0
        elif channel == 11:
            return 1
        elif channel == 13:
            return 2
        elif channel == 15:
            return 3
        elif channel == 19:
            return 4
        elif channel == 21:
            return 5
        elif channel == 23:
            return 6
        elif channel == 28:
            return 7
        else:
            return -1

    #definisco la funzione di callback generale
    def callback1(channel):
        print 'riga: ', channel, ' colonna : ', column
        i = rows(channel)
        j = columns(column)
        if(i==-1 or j==-1):
            print 'Errore nella lettura del tasto'
        else:
            print matrix[i][j]
            suono >> pb
 	time.sleep(0.7)

        
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
