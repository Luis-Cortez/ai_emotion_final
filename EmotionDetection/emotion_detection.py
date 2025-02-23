from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")
SERVICE_URL = os.getenv("SERVICE_URL")

authenticator = IAMAuthenticator( API_KEY )
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version = '2022-04-07',
    authenticator = authenticator
)

natural_language_understanding.set_service_url( SERVICE_URL )

def dominant_emotion( emotions:dict ) -> str:
    ratings = []
    for emotion in emotions:
        n = emotions[emotion]
        ratings.append( n )
    for emotion in emotions:
        if emotions[emotion] == max( ratings ):
            return emotion

def emotion_detector( text_to_analyse ):
    response = natural_language_understanding.analyze(
        text = text_to_analyse,
        features  = Features( emotion = EmotionOptions())
    ).get_result()

    emotions = response['emotion']['document']['emotion']
    dom_emotion = dominant_emotion( emotions )
    emotions["dominant_emotion"] = dom_emotion 

    return emotions


   



