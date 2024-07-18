import azure.cognitiveservices.speech as speechsdk
from config import speech_config

def recognize_speech(filename):
    audio_input = speechsdk.audio.AudioConfig(filename=filename)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
    result = recognizer.recognize_once()
    
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    else:
        return None
