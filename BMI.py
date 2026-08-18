#!/usr/bin/env python3
"""BMI Calculator

Provides a small CLI to compute Body Mass Index (BMI) with metric and
imperial unit support. Examples:

  python BMI.py --weight 70 --height 1.75
  python BMI.py --weight 154 --height 69 --unit imperial
  python BMI.py --interactive

The numeric BMI is printed along with a human-friendly category.
"""

from __future__ import annotations

import argparse
import sys
from typing import Tuple


def compute_bmi(weight_kg: float, height_m: float) -> float:
	"""Return BMI rounded to two decimals."""
	return round(weight_kg / (height_m * height_m), 2)


def bmi_category(bmi: float) -> str:
	if bmi < 18.5:
		return "Underweight"
	if bmi < 25:
		return "Normal weight"
	if bmi < 30:
		return "Overweight"
	return "Obesity"


def lbs_in_to_kg_m(weight_lbs: float, height_in: float) -> Tuple[float, float]:
	"""Convert pounds/inches to kilograms/meters."""
	kg = weight_lbs * 0.45359237
	m = height_in * 0.0254
	return kg, m


def parse_args(argv=None):
	p = argparse.ArgumentParser(description="Compute Body Mass Index (BMI)")
	p.add_argument("--weight", type=float, help="Weight (kg or lb)")
	p.add_argument("--height", type=float, help="Height (m or in)")
	p.add_argument("--unit", choices=("metric", "imperial"), default="metric",
				   help="Units: 'metric' uses kg/m, 'imperial' uses lb/in")
	p.add_argument("--interactive", action="store_true", help="Prompt for values interactively")
	return p.parse_args(argv)


def prompt_interactive() -> Tuple[float, float, str]:
	try:
		unit = input("Units (metric/imperial) [metric]: ").strip().lower() or "metric"
		if unit not in ("metric", "imperial"):
			print("Invalid unit, defaulting to 'metric'.")
			unit = "metric"

		if unit == "metric":
			weight = float(input("Weight (kg): ").strip())
			height = float(input("Height (m): ").strip())
		else:
			weight = float(input("Weight (lb): ").strip())
			height = float(input("Height (in): ").strip())

		return weight, height, unit
	except (ValueError, EOFError) as exc:
		print(f"Invalid input: {exc}")
		sys.exit(2)


def main(argv=None):
	args = parse_args(argv)

	if args.interactive or args.weight is None or args.height is None:
		weight, height, unit = prompt_interactive()
	else:
		weight, height, unit = args.weight, args.height, args.unit

	if unit == "imperial":
		weight_kg, height_m = lbs_in_to_kg_m(weight, height)
	else:
		weight_kg, height_m = float(weight), float(height)

	if weight_kg <= 0 or height_m <= 0:
		print("Weight and height must be positive numbers.")
		sys.exit(2)

	bmi = compute_bmi(weight_kg, height_m)
	category = bmi_category(bmi)

	print(f"BMI: {bmi:.2f}")
	print(f"Category: {category}")


if __name__ == "__main__":
	main()

