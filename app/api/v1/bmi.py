from fastapi import APIRouter, HTTPException
from app.schemas import BMIRequest, BMIResponse
from app.services.bmi import compute_bmi, bmi_category, lbs_in_to_kg_m

router = APIRouter()


@router.post("/", response_model=BMIResponse, summary="Calculate BMI")
async def calculate_bmi(payload: BMIRequest):
    try:
        bmi = compute_bmi(payload.weight_kg, payload.height_m)
        category = bmi_category(bmi)
        return BMIResponse(bmi=bmi, category=category)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
