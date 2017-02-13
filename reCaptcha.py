import os
import ssl
import glob
import wget
import random
import urllib
import shutil
import requests
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from flask import Flask, request

app = Flask(__name__)
@app.route("/captcha")
def captcha():
	WEB = request.args.get("web", "")	#NOTICES : GET CURRENT WEB NAME
	URL = request.args.get("url", "")	#NOTICES : GET URL
	API = request.args.get("k", "")	#NOTICES : GET API KEY
	REQ = (str(URL) + '&k=' +str(API))	#NOTICES : SET URL
	audiomp3 = (str(WEB) + '.mp3')	#NOTICES : SET STRING AND FORMAT
	audiowav = (str(WEB) + '.wav')
	audiospl = (str(WEB) + '{0}.wav')	
	urllib.request.urlretrieve(REQ, audiomp3)	#NOTICES : DOWNLOAD FROM URL
	audio = AudioSegment.from_mp3(audiomp3)	#NOTICES : CONVERT MP TO WAV
	audio.export(audiowav, format="wav")	
	sound = AudioSegment.from_wav(audiowav)	#NOTICES : SPLIT AUDIO
	chunks = split_on_silence(sound, min_silence_len=250, silence_thresh=-30, keep_silence=500)
	model = ['w','h','h']
	usage = (random.choice(model))
	r = sr.Recognizer()	
	#DISABLE	with sr.Microphone() as source:	#NOTICES : USE THE DEFAULT MICROPHONE AS THE AUDIO SOURCE, LISTEN FOR 1 SECOND TO CALIBRATE THE ENERGY THRESHOLD FOR AMBIENT NOISE LEVELS	
	#DISABLE		r.adjust_for_ambient_noise(source)
	#DISABLE		audio = r.listen(source)
	with sr.WavFile(audiowav) as source:	
		for i, chunk in enumerate(chunks):
		    out_file = ".//splitAudio//" + str(audiospl).format(i)
		    print ("Exporting : ",out_file)
		    chunk.export(out_file, format="wav")
		audio = r.record(source)		
		if str(usage) is 'g':
			try:
				value = r.recognize_google(audio, language = "en-in")	#NOTICES : TO USE ANOTHER API KEY, USE `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
				if str is bytes: 
					result = u"{}".format(value).encode("utf-8")	
				else: 
					result = "{}".format(value)
				with open("audio.log","w") as f:
					f.write("Google Speech Recognition :" + (result))
				with open("audio.his","a") as f:
					f.write("\nGoogle Speech Recognition :" + (result))
				print("Google Speech Recognition : " + (value))
			except sr.RequestError as e:
				print("Could not request from Google Speech Recognition service; {0}".format(e))
				value = ('Error : ' + str(e))		
			except sr.UnknownValueError as e:
				print("Google Speech Recognition Unknown Value Error")
				value = ('Error : ' + str(e))
		else:
			pass
		if str(usage) is 'w':
			try:
				value = r.recognize_wit(audio, key = "S7Q7D5MWGFXYIUR2AFSDTWDLNGY7HUAH")	#NOTICES : https://wit.ai/DarKWinGTM/MyFirstApp/settings
				if str is bytes: 
					result = u"{}".format(value).encode("utf-8")	
				else: 
					result = "{}".format(value)
				with open("audio.log","w") as f:
					f.write("WIT.AI : " + (result))
				with open("audio.his","a") as f:
					f.write("\nWIT.AI : " + (result))
				print("WIT.AI : " + (value))
			except sr.RequestError as e:
				print("Could not request from WIT.AI service; {0}".format(e))
				value = ('Error : ' + str(e))		
			except sr.UnknownValueError as e:
				print("WIT.AI Unknown Value Error")
				value = ('Error : ' + str(e))
		else:
			pass
		if str(usage) is 'm':
			try:
				value = r.recognize_bing(audio, key = "e1410a49826746abaed916e16ebe2e2d")	#NOTICES : https://www.microsoft.com/cognitive-services/en-US/subscriptions
				if str is bytes: 
					result = u"{}".format(value).encode("utf-8")	
				else: 
					result = "{}".format(value)
				with open("audio.log","w") as f:
					f.write("Microsoft Bring Speech : " + (result))
				with open("audio.his","a") as f:
					f.write("\nMicrosoft Bring Speech : " + (result))
				print("Microsoft Bring Speech : " + (value))
			except sr.RequestError as e:
				print("Could not request from Microsoft Bring Speech service; {0}".format(e))
				value = ('Error : ' + str(e))		
			except sr.UnknownValueError as e:
				print("Microsoft Bring Speech Unknown Value Error")
				value = ('Error : ' + str(e))
		else:
			pass
		if str(usage) is 'h':
			try:
				apimodel = ['a','b','c']
				keyusage = (random.choice(apimodel))
				if str(keyusage) is 'a': 
					value = r.recognize_houndify(audio, client_id = "909OS-u_VMMzcJm7Lkkq1g==", client_key = "oIZwTwHxvMjWVcCIxJEPmY159h72XcXsU8oUI_2ILkq_liYyrU5XBTjQN8bLKK4FhyGPfVUg0fPDh_iyURQC7A==")	#NOTICES : https://www.houndify.com/dashboard/detail/eb9e6996-6eff-4456-aec9-977c1c248e4c
				else:
					pass			
				if str(keyusage) is 'b': 
					value = r.recognize_houndify(audio, client_id = "QjRdw2gaqFXwsd2Xmyi4bQ==", client_key = "-1YcaoyfRp68lJTSZt8G5wVR9Bsndc6PD49Kd9nWpjdfRnWCxFyTRgj2G0s4uy2Ks0OoV4KquCMB9WEZbO33dw==")	#NOTICES : https://www.houndify.com/dashboard/detail/eb9e6996-6eff-4456-aec9-977c1c248e4c
				else:
					pass			
				if str(keyusage) is 'c': 
					value = r.recognize_houndify(audio, client_id = "vN0JNeEuXcY4EEjB64RC-A==", client_key = "eauh8AbNL_uVQsTiQIYO-eNkdLnLGuf-hVUokOEJkfFO6mRS5nOy6We0EoHqxQ7fhT4xuFC_BO_TCR2cRFspHw==")	#NOTICES : https://www.houndify.com/dashboard/detail/eb9e6996-6eff-4456-aec9-977c1c248e4c
				else:
					pass
				if str is bytes: 
					result = u"{}".format(value).encode("utf-8")	
				else: 
					result = "{}".format(value)
				with open("audio.log","w") as f:
					f.write("Houndify : " + (result))
				with open("audio.his","a") as f:
					f.write("\nHoundify : " + (result))					
				print("Houndify : " + (value))
			except sr.RequestError as e:
				print("Could not request from Houndify service; {0}".format(e))
				value = ('Error : ' + str(e))		
			except sr.UnknownValueError as e:
				print("Houndify Unknown Value Error")
				value = ('Error : ' + str(e))
		else:
			pass
	return value
if __name__ == "__main__":
	#DISABLE	os.system("start \"\" http://127.0.0.1:5000/captcha?url=Welcome")
	app.run(host="127.0.0.1", port=5000, threaded=True)
	app.run(processes=8)
