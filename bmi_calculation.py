
print("=== BMI Calculator ===")

weight = float(input("Enter your weight in kg: "))

feet = float(input("Enter your height (feet part only): "))
inches = float(input("Enter your height (inches part only): "))

total_inches = (feet * 12) + inches
height_in_meters = total_inches * 0.0254

bmi = weight / (height_in_meters ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
