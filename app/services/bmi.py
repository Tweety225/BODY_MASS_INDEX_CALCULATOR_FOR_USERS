from typing import Tuple


def compute_bmi(weight_kg: float, height_m: float) -> float:
    """Compute BMI and return rounded value."""
    return round(weight_kg / (height_m * height_m), 2)


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


def lbs_in_to_kg_m(weight_lbs: float, height_in: float) -> Tuple[float, float]:
    kg = weight_lbs * 0.45359237
    m = height_in * 0.0254
    return kg, m
