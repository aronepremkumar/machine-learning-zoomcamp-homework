import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Load the pipeline
with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# Define the input data model using Pydantic
class LeadInput(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# Define the prediction endpoint
@app.post("/predict")
async def predict(lead: LeadInput):
    # Convert Pydantic model to dictionary
    lead_dict = lead.dict()
    # Get probability of conversion (positive class)
    probability = pipeline.predict_proba([lead_dict])[0, 1]
    return {"probability": probability}
