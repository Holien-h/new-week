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

age = int(input("Age? "))
has_ticket = input("Do you have a ticket? (yes/no) ") == "yes"
if age >= 16 and has_ticket:
 print("Welcome to the concert!")
elif age >= 16 and not has_ticket:
 print("Buy a ticket first.")
else:
 print("Sorry, 16+ only.")
day = input("What day is it? ").lower()
if day == "saturday" or day == "sunday":
 print("It's the weekend!")

 password = input("Password: ")
if password == "python123":
 print("Access granted.")
 if len(password) < 12:
  print("Tip: use a longer password!")
else:
 print("Access denied.")