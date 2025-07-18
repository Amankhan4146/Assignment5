# === Task 1: Student Marks Lookup ===

# Step 1: Create a dictionary of student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}

# Step 2: Ask user to input a student's name
print("=== Task 1: Student Marks Lookup ===")
student_name = input("Enter the student's name: ")

# Step 3: Lookup and display marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("No record found for student:" ,student_name)
