student_name = input("Enter student name: ")

python_marks = float(input("Enter Python marks: "))
maths_marks = float(input("Enter Maths marks: "))
physics_marks = float(input("Enter Physics marks: "))
english_marks = float(input("Enter English marks: "))
c_programming_marks = float(input("Enter C Programming marks: "))

attendance = float(input("Enter attendance %: "))
family_income = float(input("Enter family income: "))

total_marks = (
    python_marks
    + maths_marks
    + physics_marks
    + english_marks
    + c_programming_marks
)
marks_percentage = total_marks / 500 * 100

if marks_percentage >= 60 and attendance >= 75 and family_income < 100000:
    print(student_name, "is eligible for scholarship")
else:
    print(student_name, "is not eligible for the scholarship")