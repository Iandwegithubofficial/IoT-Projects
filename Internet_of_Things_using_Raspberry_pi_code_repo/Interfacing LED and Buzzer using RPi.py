# Company - Seekhlo Education Pvt. Ltd.
# Author - Suruchi Gagan
# URL - cms.iandwe.in


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		 #setting up the GPIO pins to its pin number values
led = 12							 #GPIO pin number connected with LED
buzz = 26						 #GPIO pin number connected with buzzer
GPIO.setup(led,GPIO.OUT,initial=False)   #setup of led GPIO as output
GPIO.setup(buzz,GPIO.OUT,initial=False) #setup of buzzer GPIO as output

try:
	while(True):                                     #setting up a continuous while loop
		GPIO.output(led, True)		 #led turned ON
		GPIO.output(buzz, True)	 #buzzer turned ON
		print("LED and Buzzer turned ON")   #printing on status
		time.sleep(2)				 #delay of 2 seconds
		GPIO.output(led, False)	 #led turned OFF
		GPIO.output(buzz, False)	 #buzzer turned OFF
		print("LED and Buzzer turned OFF")  #printing off status
		time.sleep(2)				 #delay of 2 seconds
except KeyboardInterrupt:
	GPIO.cleanup()                           #cleanup GPIO settings before exiting
	

