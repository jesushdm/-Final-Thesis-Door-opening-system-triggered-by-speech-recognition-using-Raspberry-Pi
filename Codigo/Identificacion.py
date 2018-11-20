######################################################
# Codigo que realiza el proceso completo de identificacion, ejecutando otros archivos 
# python y verificando la contrasena. Se usa la libreria PyAudio
######################################################
# -*- coding: utf8 -*-
import time

print "___________________________________________________________________________"
print "Identifícate pronunciando la contraseña"
raw_input("Presiona enter...")

#1. Grabacion
execfile("grabacion.py")
print "Archivo audio.wav generado correctamente\n"
time.sleep(0.5)

#2. Reconocimiento de voz
execfile("reconocimiento.py")
print "Archivo transcripcion.txt generado correctamente\n"
time.sleep(0.5)


#3. Lectura de contraseña del sistema
fd_contrasena = open('contrasena.txt', 'r' )
contrasena = fd_contrasena.read()

#4. Lectura de contraseña introducida
fd_transcripcion = open('transcripcion.txt', 'r' )
introducida = fd_transcripcion.read()


#5. Si la contraseña es correcta, activa el relé (durante 1 segundo)
print "La contraseña introducida es:", introducida
time.sleep(0.5)

if introducida == contrasena:
	print "Contrasena corecta => Puerta abierta\n"
	execfile("contrasena_correcta.py")
else:
	print "Contrasena incorecta => Puerta cerrada\n"
	execfile("contrasena_incorrecta.py")

	
