#homework 1
numbergrade = float(input("Enter a number 1-4: "))

if numbergrade == 4.0:
    print("Grade: A")
elif 3.7 <= numbergrade < 4.0:
    print("Grade: A-")
elif 3.3 <= numbergrade < 3.7:
    print("Grade: B+")
elif 3.0 <= numbergrade < 3.3:
    print("Grade: B-")
elif 2.7 <= numbergrade < 3.0:
    print("Grade: C+")
elif 2.3 <= numbergrade < 2.7:
    print("Grade: C-")
elif 2.0 <= numbergrade < 2.3:
    print("Grade: D+")
elif 1.7 <= numbergrade < 2.0:
    print("Grade: D-")
else:
    print("Grade: F")
