######################################################
# Hace sonar el zumbador con un pitido largo
######################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_VERDE = 20
ZUMBADOR = 18
SENAL_RELE = 24  #La senal de control que conmutara el rele
GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(ZUMBADOR, GPIO.OUT)
GPIO.setup(SENAL_RELE, GPIO.OUT)

try:
	GPIO.output(LED_VERDE, 1)
	GPIO.output(ZUMBADOR, 1)
	GPIO.output(SENAL_RELE, 1)
	time.sleep(1)
	GPIO.output(LED_VERDE, 0)
	GPIO.output(ZUMBADOR, 0)
	GPIO.output(SENAL_RELE, 0)
except KeyboardInterrupt:
	GPIO.cleanup()
	print "\nPines GPIO puestos en estado seguro correctamente"

GPIO.cleanup()
