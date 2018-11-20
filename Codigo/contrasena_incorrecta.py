######################################################
# Hace sonar 3 veces de forma discontinua el zumbador
######################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_ROJO = 21
ZUMBADOR = 18
GPIO.setup(LED_ROJO, GPIO.OUT)
GPIO.setup(ZUMBADOR, GPIO.OUT)
	
try:
	GPIO.output(LED_ROJO, 1)
	for i in range(3):
		GPIO.output(ZUMBADOR, 1)
		time.sleep(0.2)
		GPIO.output(ZUMBADOR, 0)
		time.sleep(0.2)
	GPIO.output(LED_ROJO, 0)
except KeyboardInterrupt:
	GPIO.cleanup()
	print "\nInterrupcion, has pulsado CTRL-C. Pines GPIO reseteados correctamente"

GPIO.cleanup()
