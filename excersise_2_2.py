# ฟังก์ชันสำหรับคำนวณ BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "น้ำหนักน้อย / ผอม"
    elif 18.5 <= bmi < 23:
        return "ปกติ (สุขภาพดี)"
    elif 23 <= bmi < 25:
        return "ท้วม / อ้วนระดับ 1"
    elif 25 <= bmi < 30:
        return "อ้วน / อ้วนระดับ 2"
    else:
        return "อ้วนมาก / อ้วนระดับ 3"

# ตัวอย่างการใช้งานฟังก์ชัน
print(calculate_bmi(50, 1.75)) # ปกติ (สุขภาพดี)
print(calculate_bmi(70, 1.75)) # ท้วม / อ้วนระดับ 1
