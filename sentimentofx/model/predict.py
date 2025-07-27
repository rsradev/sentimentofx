from transformers import pipeline
from huggingface_hub import login

login(token="")


sentiment_pipeline = pipeline("sentiment-analysis")

def predict_sentiment(text: str) -> dict:
    result = sentiment_pipeline(text)[0]
    result['signal'] =  "BUY" if result['label'] == 'POSITIVE' else "SELL"
    return result
