from pydantic import BaseModel, Field, confloat


class BMIRequest(BaseModel):
    weight_kg: confloat(gt=0, lt=500) = Field(..., description="Weight in kilograms")
    height_m: confloat(gt=0, lt=3) = Field(..., description="Height in meters")


class BMIResponse(BaseModel):
    bmi: float
    category: str
