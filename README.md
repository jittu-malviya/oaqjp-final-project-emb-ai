# Emotion Detection and Prediction Project

## Overview

This project is an AI-based Emotion Detection and Prediction system developed using Python. The application analyzes user-provided text and predicts the dominant emotion expressed in the statement.

The system detects the following emotions:

* Anger
* Disgust
* Fear
* Joy
* Sadness

The project exposes an emotion detection function that can be integrated into applications, APIs, or web interfaces.

---

## Project Structure

```text
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
│
├── server.py
├── requirements.txt
├── README.md
```

---

## Requirements

Make sure Python 3.11 or later is installed.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Navigate to the project directory:

```bash
cd /home/project/final_project/oaqjp-final-project-emb-ai
```

Run Python:

```bash
python3.11
```

Import the emotion detector:

```python
from EmotionDetection.emotion_detection import emotion_detector
```

Example usage:

```python
text = "I am very happy today"
result = emotion_detector(text)
print(result)
```

---

## Sample Output

```python
{
    'anger': 0.01,
    'disgust': 0.02,
    'fear': 0.03,
    'joy': 0.90,
    'sadness': 0.04,
    'dominant_emotion': 'joy'
}
```

---

## Features

* Detects emotions from text input
* Predicts dominant emotion
* Modular Python package structure
* Easy integration with Flask or APIs
* Clean and reusable codebase

---

## Technologies Used

* Python 3.11
* Natural Language Processing (NLP)
* Flask (optional)
* IBM Watson NLP API / Emotion Analysis

---

## Author

Developed as part of th
