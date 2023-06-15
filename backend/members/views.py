from django.http import JsonResponse
from django.shortcuts import render
from joblib import load
from transformers import pipeline

model = load('./model/sentiment_analysis.pkl')
sent_pipeline = pipeline("sentiment-analysis")


def predict_view(request):
    # print('request', request)
    return render(request, 'predict.html')

def predict_sentiment(request):
    if request.method == 'GET':
        # Get the input word from the request parameters
        input_word = request.GET.get('word', '')

        # Use the sentiment analysis pipeline to predict the sentiment
        result = sent_pipeline(input_word)

        # Extract the label and score from the prediction result
        label = result[0]['label']
        score = result[0]['score']

        # Return the prediction result as a JSON response
        response = {
            'label': label,
            'score': score
        }
        return JsonResponse(response)
