"""
A Flask web application for detecting emotions in text.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask("__name__")

@app.route("/")
def render_index_page():
    """
    Renders the home page (index.html).
    Returns:
        str: Rendered HTML page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def get_emotion_detector():
    """
    Detects emotions from the provided text and returns the result.
    Query Parameters:
        textToAnalyze (str): The input text to analyze.
    Returns:
        str: A formatted string describing the detected emotions, or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detection.emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_str = f"For the given statement, the system response is " \
                   f"'anger': {result['anger']},'disgust': {result['disgust']}" \
                   f", 'fear': {result['fear']}, 'joy': {result['joy']} "\
                   f"and 'sadness': {result['sadness']}. "\
                   f"The dominant emotion is {result['dominant_emotion']}."

    return response_str

if __name__ == '__main__':
    app.run(debug=True)
