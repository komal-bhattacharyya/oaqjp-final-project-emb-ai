import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    #url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #header= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    #print(response.status_code)
    #return response.text
    response_modi = json.loads(response.text)
    output_res = response_modi['emotionPredictions'][0]['emotion']
    name_dominant_emotion = max(output_res, key = output_res.get)
    #output_res['dominant_emotion'] = name_dominant_emotion
    # If the response status code is 200, extract the label and score from the response
    # Define the first payload with nonsensical text to test the API
    myobj = { "raw_document": { "text": "as987da-6s2d aweadsa" } }

    # Make a POST request to the API with the first payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Print the status code of the first response
    print(response.status_code)

    # Define the second payload with a meaningful text to test the API
    myobj = { "raw_document": { "text": "Testing this application for error handling" } }
    # Make a POST request to the API with the second payload and headers
    response = requests.post(url, json=myobj, headers=header)
    print(response.status_code)
    
    if response.status_code == 200:
        output_res['dominant_emotion'] = name_dominant_emotion
    
    elif response.status_code == 400:
        output_res = {k:None for k in output_res}
        output_res['dominant_emotion'] = None    
    
    # For any other unexpected status codes, set label and score to None
    else:
        output_res = {k:None for k in output_res}
        output_res['dominant_emotion'] = None
    
    return output_res
