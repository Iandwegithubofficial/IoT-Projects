# Company - Seekhlo Education Pvt. Ltd.
# Author - Suruchi Gagan
# URL - cms.iandwe.in


import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11		# Set sensor type : Options are DHT11,DHT22 or AM2302
 
gpio = 25						# Set GPIO sensor is connected to
 
'''Use read_retry method. This will retry up to 15 times to
get a sensor reading (waiting 2 seconds between each retry).'''
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
try:
	while True:
		if humidity is not None and temperature is not None:
  			print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))		#printing the values
		else:
  			print('Failed to get reading. Try again!')										#printing error message
		time.sleep(1)					#delay of 1 second

except KeyboardInterrupt:
	print("Ending Code")				#printing end code message
