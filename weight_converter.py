weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
else:
    print(f"{unit} is not valid")
    
print(f"Your weight is : {round(weight, 1)} {unit}")