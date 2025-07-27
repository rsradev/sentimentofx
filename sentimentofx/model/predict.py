from transformers import pipeline
from huggingface_hub import login
import os
from dotenv import load_dotenv


load_dotenv()
login(token=os.getenv("HUGGINGFACE_TOKEN"))

sentiment_pipeline = pipeline(
    "sentiment-analysis"

)

def predict_sentiment(text: str) -> dict:
    result = sentiment_pipeline(text)[0]
    result['signal'] =  "BUY" if result['label'] == 'POSITIVE' else "SELL"
    return result
