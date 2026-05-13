import requests
import json

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    input_json = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }
    res = requests.post(url=url, headers=headers, json=input_json)
    res_json = res.json()
    
    emotions = res_json['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    joy_score = emotions['joy']
    fear_score = emotions['fear']
    disgust_score = emotions['disgust']
    sadness_score = emotions['sadness']
    dominant_emotion = { 'dominant_emotion': 0}

    max_score = 0
    for emotion, value in emotions.items():
        if max_score < value:
            max_score = value
            dominant_emotion['dominant_emotion'] = emotion

    emotion_scores = { 
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score, 
        'joy': joy_score, 
        'sadness': sadness_score,      
        'dominant_emotion': dominant_emotion['dominant_emotion']
    }

    return emotion_scores