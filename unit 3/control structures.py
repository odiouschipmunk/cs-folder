grade = int(input("grade: "))
letter_grade = (
    "a"
    if grade >= 90
    else "b"
    if grade >= 80
    else "c"
    if grade >= 70
    else "d"
    if grade >= 60
    else "f"
)
print(f"letter grade: {letter_grade}")
