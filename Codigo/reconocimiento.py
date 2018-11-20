######################################################
# Codigo que toma el audio grabado, lo envia mediante la API de Google, y recibe el resultado como String
# Necesario instalar la libreria de Google ->  sudo pip install --upgrade google-cloud-speech
# (La otra opcion seria hacerlo con REST https://cloud.google.com/apis/docs/overview)
######################################################
# -*- coding: utf8 -*-

#0. Importar librerias 
import io
import os
from google.cloud         import speech
from google.cloud.speech  import enums
from google.cloud.speech  import types

#1. Nombres de archivo
ARCHIVO_ENTRADA = "audio.wav"
ARCHIVO_SALIDA="transcripcion.txt"

#2. Establece la configuracion para la instruccion de reconocimiento de voz
config = types.RecognitionConfig(
	    encoding                 = enums.RecognitionConfig.AudioEncoding.LINEAR16,
	    sample_rate_hertz = 16000,
	    language_code      ='es-ES')

#3.  Carga el audio en memoria
with io.open(ARCHIVO_ENTRADA, 'rb') as audio_file:
	    content = audio_file.read()
	    audio = types.RecognitionAudio(content=content)

#4. Realiza el reconocimiento de la voz con la configuracion indicada, sobre el audio indicado
print "Realizando reconocimiento de voz..."
client = speech.SpeechClient()
response = client.recognize(config, audio)
transcripcion = response.results[0].alternatives[0].transcript
transcripcion = transcripcion.strip()  #Aplicamos el metodo strip() para eliminar los (posibles) espacios iniciales y finales

#5. Escribe a archivo de texto
archivo= open(ARCHIVO_SALIDA, "w")
archivo.write(transcripcion.encode('utf-8' , 'replace') )
archivo.close() 

