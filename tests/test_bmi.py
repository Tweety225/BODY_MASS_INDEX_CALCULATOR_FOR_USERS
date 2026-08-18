from app.services.bmi import compute_bmi, lbs_in_to_kg_m


def test_compute_bmi_metric():
    bmi = compute_bmi(70, 1.75)
    assert round(bmi, 2) == 22.86


def test_lbs_in_conversion():
    kg, m = lbs_in_to_kg_m(154, 69)
    assert round(kg, 2) == round(154 * 0.45359237, 2)
    assert round(m, 3) == round(69 * 0.0254, 3)
