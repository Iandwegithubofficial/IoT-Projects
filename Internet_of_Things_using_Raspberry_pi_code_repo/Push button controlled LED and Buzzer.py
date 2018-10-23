# Company - Seekhlo Education Pvt. Ltd.
# Author - Suruchi Gagan
# URL - cms.iandwe.in


import RPi.GPIO as GPIO

GPIO.setwarnings(False)			#Setting Warnings to False
GPIO.setmode(GPIO.BOARD)		#Setting up the GPIO pin access using Board Number
push1 = 12						#Starting Push Button
push2 = 16						#Stoping Push Button
led = 8							#Led GPIO pin Number
buzzer = 10						#buzzer GPIO pin Number

GPIO.setup(push1,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)	#push1 to input with initial value 0
GPIO.setup(push2,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)	#push2 to input with initial value 0
GPIO.setup(led,GPIO.OUT,initial = False)						#led to output with initial value 0
GPIO.setup(buzzer,GPIO.OUT,initial = False)					#buzzer to output with initial value 0
try:
	while True:
		if(GPIO.input(push1) == 1):							#Condition to check if button 1 pushed or not
			GPIO.output(led,True)							#led turned ON
			GPIO.output(buzzer,True)						#buzzer turned ON
			print("System switched On")					#Printing message
			while(GPIO.input(push2) == 0):					#Wait till button 2 is pressed
				pass									#just passing
			GPIO.output(led,False)						#Turn led OFF
			GPIO.output(buzzer,False)						#Turn buzzer OFF
			print("System switched Off")					#Display message of turning OFF

except KeyboardInterrupt:
	print("Program stopped")
	GPIO.cleanup()										#Cleaning GPIO configurations
			
