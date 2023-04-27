# 딕셔너리(Dictionaries)

student = {
    "student_no" : "202301234",
    "major": "English",
    "grade": 1
}

# print(student["student_no"])

# student["student_no"] = "202301235"

# print(student)
# print(student["student_no"])

# 추가
student["gpa"] = 4.5
print(student)

# 수정
student["gpa"] = 4.3
print(student)

# 삭제 
del student["grade"]
print(student)