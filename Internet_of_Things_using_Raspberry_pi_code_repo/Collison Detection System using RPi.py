# Company - Seekhlo Education Pvt. Ltd.
# Author - Suruchi Gagan
# URL - cms.iandwe.in


import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)		#Setting Warning to false
GPIO.setmode(GPIO.BOARD)	#Setting pin mode of GPIO to Board Number

trig = 32			#trigger GPIO pin number
echo = 38		#techo GPIO pin number
led1 = 12		#led1 GPIO pin number
led2 = 10		#led2 GPIO pin number
led3 = 8			#led3 GPIO pin number
buzzer = 18		#buzzer pin number
critical =25		#setting critical distance value in cm
threshold = 75	#setting threshhold distance value in cm


GPIO.setup(trig,GPIO.OUT,initial=False)			#setting trig as output
GPIO.setup(echo,GPIO.IN)						#setting echo as input
GPIO.setup(led1,GPIO.OUT,initial = False)		#setting led1 as output
GPIO.setup(led2,GPIO.OUT,initial = False)		#setting led2 as output
GPIO.setup(led3,GPIO.OUT,initial = False)		#setting led3 as output
GPIO.setup(buzzer,GPIO.OUT,initial = False)		#setting buzzer as output

print("Starting up Collision Detection System")	#printing message
time.sleep(2)									#delay of 2 seconds for the first time

try:
	while True:
		time.sleep(0.1)				# delay to avoid 100% usage of CPU
		GPIO.output(trig, True)			#Set TRIG as HIGH
		time.sleep(0.00001)			#Delay of 0.00001 seconds
		GPIO.output(trig, False)		#Set TRIG as LOW
	
		while GPIO.input(echo)==0:	#Check whether the ECHO is LOW
			pulse_start = time.time()	#Saves the last known time of LOW pulse

		while GPIO.input(echo)==1:	#Check whether the ECHO is HIGH
			pulse_end = time.time()	#Saves the last known time of HIGH pulse 

		pulse_duration = pulse_end - pulse_start		#Get pulse duration to a variable

  		distance = pulse_duration * 17150			#Multiply pulse duration by 17150 to get distance
  		distance = round(distance, 2)				#Round to two decimal points

  		if distance > 2 and distance < 400:			#Check whether the distance is within range
    			if(distance <=critical):					#If distance is less than critical value turn on led1,led2,led3 and buzzer
				GPIO.output(led1,True)
				GPIO.output(led2,True)
				GPIO.output(led3,True)
				GPIO.output(buzzer,True)
				print ("!!!Obstacle very close at a distance of: ",distance," cm, so prevent collision")		#Printing message and distance
			elif(distance >critical and distance <= threshold):		#If distance lies between critical and threshold turn led1,led2,buzzer ON and led3 OFF
				GPIO.output(led1,True)
				GPIO.output(led2,True)
				GPIO.output(led3,False)
				time.sleep(0.3)								#giving a definite pattern to buzzer
				GPIO.output(buzzer,True)						#buzzer ON
				time.sleep(0.3)
				GPIO.output(buzzer,False)						#buzzer OFF
				print ("!Obstacle coming close and is currently at a distance: ",distance," cm")	#Printing message and distance
			elif( distance > threshold):							#If distance is greater than threshold turn only led1 ON
				GPIO.output(led1,True)
				GPIO.output(led2,False)
				GPIO.output(led3,False)
				GPIO.output(buzzer,False)
				print ("Obstacle very far at a distance of: ",distance," cm, so chill out")	#Printing Message and distance
  		else:
    			print "Out Of Range"                   #display out of range

except KeyboardInterrupt:
	print('Code Stopped')
	GPIO.cleanup()						#cleanup GPIO settings before exiting
		


