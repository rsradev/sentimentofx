from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    label: str
    signal: str
    score: float
    