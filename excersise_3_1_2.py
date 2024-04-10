# รับข้อมูลเข้ามาเป็นตัวเลขจากผู้ใช้
countdown_start = int(input("กรุณาป้อนตัวเลขเริ่มต้นสำหรับการนับถอยหลัง: "))

# ตรรกะการนับถอยหลังโดยใช้ while loop
while countdown_start >= 0:
    print(countdown_start)
    countdown_start -= 1  # ลดค่านับลง
