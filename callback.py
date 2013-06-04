import RPi.GPIO as GPIO
import time

#definsco la numerazione dei pin
GPIO.setmode(GPIO.BOARD)

#imposto il pin 3 come entrata (pull up)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#definisco i channel per le callback in entrata
channels = [3, 5, 7, 11, 13, 15, 19, 21]
#definisco il numero di colonna
column = 0

#definisco la funzione di callback per il gpio3
def callback1(channels[0]):
    print 'colonna = ', column

def callback2(channels[1]):
    print 'colonna = ', column

def callback3(channels[2]):
    print 'colonna = ', column

def callback4(channels[3]):
    print 'colonna = ', column

def callback5(channels[4]):
    print 'colonna = ', column

def callback6(channels[5]):
    print 'colonna = ', column

def callback7(channels[6]):
    print 'colonna = ', column

def callback8(channels[7]):
    print 'colonna = ', column


#event detect delle callback
GPIO.add_event_detect(channel1, GPIO.RISING)
GPIO.add_event_detect(channel2, GPIO.RISING)
GPIO.add_event_detect(channel3, GPIO.RISING)
GPIO.add_event_detect(channel4, GPIO.RISING)
GPIO.add_event_detect(channel5, GPIO.RISING)
GPIO.add_event_detect(channel6, GPIO.RISING)
GPIO.add_event_detect(channel7, GPIO.RISING)
GPIO.add_event_detect(channel8, GPIO.RISING)
#aggiungo le callback con bouncetime=300ms
GPIO.add_event_callback(channel1, callback1, bouncetime=300)
GPIO.add_event_callback(channel2, callback2, bouncetime=300)
GPIO.add_event_callback(channel3, callback3, bouncetime=300)
GPIO.add_event_callback(channel4, callback4, bouncetime=300)
GPIO.add_event_callback(channel5, callback5, bouncetime=300)
GPIO.add_event_callback(channel6, callback6, bouncetime=300)
GPIO.add_event_callback(channel7, callback7, bouncetime=300)
GPIO.add_event_callback(channel8, callback8, bouncetime=300)

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
        time.sleep(20)     
        GPIO.output(ch_out, GPIO.LOW)
    time.sleep(140)
GPIO.cleanup()
