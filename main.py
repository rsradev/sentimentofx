from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from sentimentofx.appdb import models, schemas, db
from sentimentofx.model import predict

models.Base.metadata.create_all(bind=db.engine)
app = FastAPI()

def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@app.post("/predict", response_model=schemas.PredictionOutput)
def predict_sentiment_route(input: schemas.TextInput, db: Session = Depends(get_db)):
    result = predict.predict_sentiment(input.text)
    pred = models.Prediction(text=input.text, label=result["label"], score=result["score"])
    db.add(pred)
    db.commit()
    return result