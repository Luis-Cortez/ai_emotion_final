"""importing needed modules"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index() -> str:
    """rendering index.html template """
    return render_template("index.html")

@app.route("/emotionDetector", methods = ['GET'])
def emotion_detect() -> dict:
    """ Analyzing emotions"""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return emotions
