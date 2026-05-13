""" This module launches the server """

# Importing the necessary libraries to run the application
from flask import Flask, render_template, request
# Importing the package that holds the logic to run the api
from EmotionDetection.emotion_detection import emotion_detector

# Initializing the Flask object to the app variable
app = Flask(__name__)

# Defining the root '/' route to display the index.html file
@app.route('/')
def index():
    """ Returning the .html file to display """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_function():
    """ Function that calls the package function to return an emotional analysis"""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    emotion_analysis = f"""
        For the given statement, the system response is 'anger': {emotions['anger']},
        'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 
        'joy': {emotions['joy']}, 'sadness': {emotions['sadness']}. 
        The dominant emotion is {emotions['dominant_emotion']}."""
    if emotions['dominant_emotion'] is None:
        emotion_analysis = "Invalid input! Try again."
    
    return emotion_analysis
if __name__ == "__main__":
    app.run(debug=True, port=5000)