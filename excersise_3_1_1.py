# ขอให้ผู้ใช้ป้อนข้อมูลเข้ามาเป็นตัวเลข
countdown_start = int(input("กรุณาป้อนตัวเลขเริ่มต้นสำหรับการนับถอยหลัง: "))

# ตรรกะการนับถอยหลังโดยใช้ for loop
for number in range(countdown_start, -1, -1):
    print(number)
