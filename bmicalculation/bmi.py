from httplib2 import Response


json = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
]

Under_weight = 18.4
Normal_weight = 24.9
Over_weight = 29.9
Moderately_obese = 34.9
Severely_obese = 39.9
Very_severely_obese = 40

persons = {
    "under_weight": 0, 
    "noremal_weight": 0, 
    "over_weight": 0,
    "moderately_obese": 0,
    "severly_obese": 0,
    "very_serverly_obese": 0
}
json1 = []

def bmi_caluculation():
    for i in json:
        BMI = i["WeightKg"]/(i["HeightCm"]/100)**2
        
        if BMI <= Under_weight:
            persons["under_weight"] += 1
            i["bmi_category"] = "under_weight"
            i["bmi"] = BMI
            i["health_risk"] = "malnutrition_risk"
        
        elif BMI>Under_weight and BMI<=Normal_weight:
            persons["noremal_weight"] += 1
            i["bmi_category"] = "normal_weight"
            i["bmi"] = BMI
            i["health_risk"] = "low_risk"

        elif BMI>=Normal_weight and BMI<=Over_weight:
            persons["over_weight"] += 1
            i["bmi_category"] = "over_weight"
            i["bmi"] = BMI
            i["health_risk"] = "enhanced_risk"

        elif BMI>Over_weight and BMI<=Moderately_obese:
            persons["moderately_obese"] += 1
            i["bmi_category"] = "moderately_obese"
            i["bmi"] = BMI
            i["health_risk"] = "medium_risk"
        
        elif BMI>Moderately_obese and BMI<=Severely_obese:
            persons["severly_obese"] += 1
            i["bmi_category"] = "severly_obese"
            i["bmi"] = BMI
            i["health_risk"] = "high_risk"
        
        else:
            persons["very_serverly_obese"] += 1
            i["bmi_category"] = "very_severly_obese"
            i["bmi"] = BMI
            i["health_risk"] = "very_high_risk"
    print(json)
    return Response(persons)

result = bmi_caluculation()
print(result)
