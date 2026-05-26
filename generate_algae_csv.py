"""Generate a synthetic algae growth CSV similar to the GUI simulation.
Usage: python generate_algae_csv.py [days]
"""
import csv
import random
import os
import sys

def generate(days=30, out_path="datasets/algae_growth_data.csv"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    soil_types = ["Iron-rich", "Sulfate-based", "Clay-based"]
    enzyme_types = ["Chromate Reductase", "Class II Chromate Reductase", "Urease"]
    temperature = 20
    co2_level = 0.05
    light_hours = 9

    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["day","soil","enzyme","temperature","co2","light","growth_rate","oxygen_output"])
        for day in range(1, days+1):
            soil_type = soil_types[(day - 1) % len(soil_types)]
            enzyme_type = enzyme_types[(day - 1) % len(enzyme_types)]
            base_growth = round(random.uniform(2.0, 5.0), 3)
            base_oxygen = round(random.uniform(10.0, 25.0), 3)
            writer.writerow([day, soil_type, enzyme_type, temperature, co2_level, light_hours, base_growth, base_oxygen])
    return out_path

if __name__ == "__main__":
    days = 30
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            print("Invalid days argument, using 30.")
    path = generate(days=days)
    print(f"Generated CSV: {path} ({days} rows)")
