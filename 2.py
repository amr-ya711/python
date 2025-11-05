import pandas as pd

students_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 22, 19, 21, 20],
    "Grade": ["A", "B", "A", "C", "B"],
    "Marks": [85, 78, 92, 65, 74]
})

first_three = students_data.head(3)                
name_marks = students_data[["Name", "Marks"]]      
grade_A_students = students_data[students_data["Grade"] == "A"]  

print("\nFirst 3 rows:\n", first_three)
print("\nName and Marks columns:\n", name_marks)
print("\nStudents with Grade A:\n", grade_A_students)
