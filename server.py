"""
Emotion Detection Server
This script defines a Flask server for performing emotion detection on custom input text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the custom input text for emotions and return formatted message.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response \n"
        f"'anger': {formated_response['anger']}, \n"
        f"'disgust': {formated_response['disgust']}, \n"
        f"'fear': {formated_response['fear']}, \n"
        f"'joy': {formated_response['joy']}, \n"
        f"'sadness': {formated_response['sadness']}.\n"
        f"The dominant emotion is "
        f"{formated_response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Index Page Rendering."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
