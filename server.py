'''This module is the server for the Emotion Detector Web App'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/')
def render_index():
    '''This renders the index template'''
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    '''This performs the detection of emotion'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again"
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, \
        'disgust': {response['disgust']}, 'fear': {response['fear']}, \
        'joy': {response['joy']} and 'sadness': {response['sadness']}. \
        The dominant emotion is {response['dominant_emotion']}." )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
