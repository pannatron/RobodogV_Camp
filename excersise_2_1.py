# ฟังก์ชันสำหรับคำนวณเกรดจากคะแนน
def calculate_grade(score):
    if 80 <= score <= 100:
        return "A grade"
    elif 60 <= score <= 79:
        return "B grade"
    elif 40 <= score <= 59:
        return "C grade"
    elif 20 <= score <= 39:
        return "D grade"
    elif 0 <= score <= 19:
        return "F grade"
    else:
        return "Invalid score"

# ตัวอย่างการใช้งานฟังก์ชัน
print(calculate_grade(85))
print(calculate_grade(75))
print(calculate_grade(45))
print(calculate_grade(25))
print(calculate_grade(10))
