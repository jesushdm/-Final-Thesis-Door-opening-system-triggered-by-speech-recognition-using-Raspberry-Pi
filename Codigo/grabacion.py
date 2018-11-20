######################################################
# Codigo que realiza la captura de audio. Se usa la libreria PyAudio
######################################################
# -*- coding: utf8 -*-
#0. Importar librerias
import pyaudio
import wave
from array import array
import time
from math import  sqrt

def RMS(vector):
	return sqrt( sum(n*n for n in bloque) / len(bloque) )

#1. Parametros de la grabacion
FORMATO=pyaudio.paInt16
CANALES=1
TASA_MUESTREO=16000
SEGMENTO=1024
DURACION=3
NOMBRE_ARCHIVO="audio.wav"

#2. Inicializacion de PyAudio
audio = pyaudio.PyAudio() 
stream = audio.open(format = FORMATO,
		    channels = CANALES,
		    rate = TASA_MUESTREO,
	            input = True,
	            frames_per_buffer = SEGMENTO)
frames=[] 

#3. Se estara "capturando" todo el rato el sonido  con el microfono (pero sin grabarlo) y comprobando si supera un umbral...
UMBRAL = 3000
print "\nValor umbral actual: RMS =", UMBRAL 
print "Esperando superar umbral...\n"

bytes = stream.read(SEGMENTO)
bloque = array('h', bytes)  #Necesitamos poner los bytes grabados por el microfono en forma de array, para hallar el max
valorRMS=  RMS(bloque)
print "Valor RMS =", valorRMS
valorRMSmax = valorRMS

while (valorRMS < UMBRAL):
	bytes = stream.read(SEGMENTO)
	bloque = array('h', bytes)
	valorRMS= RMS(bloque)
	if valorRMS > valorRMSmax:
		valorRMSmax = valorRMS
		print "Valor RMS maximo detectado =", valorRMSmax
		
	

#4. ...Y cuando se supere este umbral (se anula la condicion del while) empezaremos a guardar los datos    
print "Grabando audio..."
for i in range(0, TASA_MUESTREO/SEGMENTO * DURACION):    
        bytes = stream.read(SEGMENTO)
        frames.append(bytes)
        

print("Grabacion finalizada") 
time.sleep(0.5)

#5. Termina la grabacion
stream.stop_stream()
stream.close()
audio.terminate()
#6. Escritura a archivo
wavfile=wave.open(NOMBRE_ARCHIVO, 'wb')
wavfile.setnchannels(CANALES)
wavfile.setsampwidth(audio.get_sample_size(FORMATO))
wavfile.setframerate(TASA_MUESTREO)
wavfile.writeframes(b''.join(frames))
wavfile.close()
