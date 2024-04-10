# รับค่าความสูงของปิรามิดจากผู้ใช้
height = int(input("Enter the height of the pyramid: "))

# กำหนด list ของข้อมูลที่จะใช้ในแต่ละชั้นของปิรามิด
data_list = ['a', 'b', 'c', 'd']

# สร้างปิรามิดโดยใช้ loop
for i in range(1, height + 1):
    # สร้างสตริงสำหรับแต่ละบรรทัดของปิรามิด
    line_list = []
    index = 0  # ตัวแปรเพื่อติดตามตำแหน่งใน data_list
    for j in range(i):
        # เพิ่มองค์ประกอบจาก data_list โดยคำนึงถึงการวนรอบ
        if index == len(data_list):  # ถ้า index เท่ากับขนาดของ data_list, วนกลับไปที่ต้น
            index = 0
        line_list.append(data_list[index])
        index += 1
    
    # สร้างสตริงสำหรับปิรามิด: จัดเรียงปกติและสลับด้าน
    line_string = ''.join(line_list + line_list[-2::-1])  # สร้างสตริงแบบสมมาตร
    
    # พิมพ์แต่ละแถวของปิรามิด, จัดกึ่งกลางด้วย rjust
    print(line_string.center(height * 2 - 1 + len(line_string)//2))
