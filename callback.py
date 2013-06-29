#!/usr/bin/env python2.7  

#Import delle Librerie
import RPi.GPIO as GPIO #lib. GPIO
import time #lib. time
from Nsound import * #lib. suono

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

#Matrice contenente le frequenze dei vari suoni
matrix = [
[ 66, 70, 74, 78, 83, 88, 93, 98],     
[104,110,117,124,131,139,147,156],  
[165,175,158,196,208,220,233,247],    
[262,277,294,311,330,349,370,392],
[415,440,466,494,523,554,587,622],
[659,698,740,784,831,880,932,988],
[1046,0,0,0,0,0,0,0]]

matrix2 = [
[ 1, 2, 3, 4, 5, 6, 7, 8],
[ 9,10,11,12,13,14,15,16],
[17,18,19,20,21,22,23,24],
[25,26,27,28,29,30,31,32],
[33,34,35,36,37,38,39,40],
[41,42,43,44,45,46,47,48],
[49,-1,-1,-1,-1,-1,-1,-1]]


#imposto i channels come input (pull down virtuale)
GPIO.setup(channel1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#definisco il numero di colonna
column = 0

#program header printed on the screen
try:
    #definisco la frequenza a cazzo
    sr = 44100.0
    #def. la sinusoide
    sine = Sine(sr)
    #definisco il suono


for d1 in range(6):
    for d2 in range(6):

    suono = sine.generate(0.2,440.0)
    #definisco il playback 
    pb = AudioPlayback(sr, 1, 16)

    print "Callback reading example for MickFenneck's HighSchool Final Project"
    print "GPIO IN:  7, 11, 13, 15, 19, 21, 23\n"
    print "GPIO OUT: 8, 10, 12, 16, 18, 22, 24, 26\n"
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
        elif channel == 26:
            return 7
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
        else:
            return -1

    #definisco la funzione di callback generale
    def callback1(channel):
        #print 'riga: ', channel, ' colonna : ', column
        i = rows(channel)
        j = columns(column)
        if(i==-1 or j==-1):
            print 'Errore nella lettura del tasto'
        else:
            print 'i = ',(i+1),' j = ',(j+1)
            print matrix2[i][j]
            print matrix[i][j]

    #event detect per i diversi canali (tempo di attesa 150 ms)
    GPIO.add_event_detect(channel1, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel2, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel3, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel4, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel5, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel6, GPIO.RISING, callback=callback1, bouncetime=150)
    GPIO.add_event_detect(channel7, GPIO.RISING, callback=callback1, bouncetime=150)
    
    print "The program will now start..."
    #numero dei pin in uscita
    pin_out = [8, 10, 12, 16, 18, 22, 24, 26]
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
            suono >> pb
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
print "\n================================== the end ======================================"
