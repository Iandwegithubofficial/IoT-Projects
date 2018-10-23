# Company - Seekhlo Education Pvt. Ltd.
# Author - Suruchi Gagan
# URL - cms.iandwe.in


import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)			#to set GPIO Warnings at the starting to false
GPIO.setmode(GPIO.BOARD)		#setting up the GPIO system to board number

trig = 22			#trig pin is 22 board number gpio
echo = 26		#echo pin is 26 board number gpio

GPIO.setup(trig,GPIO.OUT,initial=False)		#setting trig as output gpio
GPIO.setup(echo,GPIO.IN)					#setting echo as input gpio

print("Starting up distance measurement")	#starting message
time.sleep(2)								#delay for the ultrasonic to settle down

try:
	while True:
		time.sleep(0.2)				 #a delay to avoid 100% CPU usage
		GPIO.output(trig, True)                  #Set TRIG as HIGH
		time.sleep(0.00001)                      #Delay of 0.00001 seconds
		GPIO.output(trig, False)                #Set TRIG as LOW
	
		while GPIO.input(echo)==0:               #Check whether the ECHO is LOW
			pulse_start = time.time()            #Saves the last known time of LOW pulse

		while GPIO.input(echo)==1:               #Check whether the ECHO is HIGH
			pulse_end = time.time()             #Saves the last known time of HIGH pulse 

		pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
		distance = pulse_duration * 17150		#Multiply pulse duration by 17150 to get the distance
		distance = round(distance, 2)			#Round to two decimal points

		if (distance > 2 and distance < 400):       #Check whether the distance is within range
			print ("Distance: ",distance," cm")    #Print the distance
		else:
			print ("Out Of Range")                     #display out of range

except KeyboardInterrupt:
	GPIO.cleanup()						#cleanup GPIO settings before exiting
