import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[16].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	
	if hour >= 5 and hour < 12:
		speak("Good Morning!")

	elif hour>=12 and hour < 17:
		speak("Good Afternoon")

	else:
		speak("Good Evening")
	
	speak("I am Jarvis Sir.Please tell me how can help I you today")

def main():
	speak('Hello Anik! Hi how can I help you today')

def takeCommand():
	# It takes microphones input from the user and returns strings output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		# r.pause_threshold = 1
		# r.dynamic_energy_threshold = True
		# r.energy_threshold = 150
		audio = r.listen(source)

	try:
		print("recognizing...")
		query = r.recognize_google(audio, Language='en-US')
		print("user said:{query}\n")

	except Exception as e:
		# print(e)
		print("Say that again please...")
		return None
	return query

if __name__ == "__main__":
	wishMe()
	while True:
	# main()
		# query = takeCommand().lower()
		print(takeCommand())
		# logic for excuting takes based on query
		if "wikipedia" in query:
			speak("Searching Wikipedia...")
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query, sentences=2)
			speak("according to Wikipedia")
			speak(results)

		elif"open youtube" in query:
			webbrowser.open("youtube.com")

		elif"open google" in query:
			webbrowser.open("google.com")
		elif "the time" in query:
			strTime = datetime.datetime.now().strftime("%H,%M,%S")
		speak(f"Sir, The Time is {strTime}")
