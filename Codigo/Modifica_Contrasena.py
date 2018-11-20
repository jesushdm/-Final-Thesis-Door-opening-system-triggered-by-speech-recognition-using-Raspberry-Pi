######################################################
# Codigo que realiza la modificacion de contrasena, comprobando que la transcripcion 
# del reconocimiento de voz coincida correctamente con la introducida por teclado
######################################################
# -*- coding: utf8 -*-
import time

#1. Introduccion nueva contraseña
print "___________________________________________________________________________"
print "Cambio de contraseña. Pulsa ENTER para introducir una nueva..."
nueva_contrasena = raw_input("")

#2. Realiza la transcripcion de voz de la nueva contrasena
#2(a). Grabacion de audio
raw_input("A continuacion, pronuncia la contraseña en voz alta. Si la transcripcion no coincide con la que introdujiste, no se podra actualizar y deberas volver a intentarlo\n")
execfile("grabacion.py")
print "Archivo audio.wav generado correctamente\n"
time.sleep(0.5)
#2(b). Reconocimiento de voz
execfile("reconocimiento.py")
print "Archivo transcripcion.txt generado correctamente\n"
time.sleep(0.5)
#2(c). Lectura de la transcripcion
fd_transcripcion = open('transcripcion.txt', 'r' )
transcripcion = fd_transcripcion.read()

#3. Si la transcripcion del audio coincide con la contrasena escrita => La actualiza
if transcripcion == nueva_contrasena:
	print "La transcripcion coincide con la contraseña introducida. Contraseña actualizada."
	archivo = open("contrasena.txt", "w")
	archivo.write(transcripcion.encode('utf-8' , 'replace') )
	archivo.close()
else:
	print "La transcripcion no coincide con la contraseña introducida. La contraseña no se pudo actualizar, intentelo de nuevo"
