score = int(input("Score: "))


if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score <= 90:
    print("Grade: B")
elif score >= 70 and score <= 80:
    print("Grade: C")
elif score >= 60 and score <= 70:
    print("Grade: D")
elif score >= 0 and score <= 60:
    print("Grade: F")
else:
    print("Give score between 0 to 100")