score = int(input("Your test score (0-100)? "))
if score >= 90:
 grade = "A"
elif score >= 75:
 grade = "B"
elif score >= 50:
 grade = "C"
else:
 grade = "F"
print(f"Your grade: {grade}")