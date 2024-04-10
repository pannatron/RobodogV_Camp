# รับค่าความสูงของปิรามิดจากผู้ใช้
height = int(input("Enter the height of the pyramid: "))

# กำหนด list ของข้อมูลที่จะใช้ในแต่ละชั้นของปิรามิด
data_list = ['a', 'b', 'c', 'd']

# สร้างปิรามิดโดยใช้ loop
for i in range(1, height + 1):
    # สร้างสตริงสำหรับแต่ละบรรทัดของปิรามิด
    line_string = ''
    index = 0
    for j in range(i):
        if index >= len(data_list):
            index = 0
        line_string += data_list[index]
        index += 1
    for j in range(i-2, -1, -1):
        if j >= len(data_list):
            j %= len(data_list)
        line_string += data_list[j]

    # การจัดกึ่งกลางโดยไม่ใช้ .center()
    # คำนวณช่องว่างก่อนข้อความ
    leading_spaces = ' ' * ((height * 2 - 1 + (i - 1)) // 2 - i)
    # พิมพ์แต่ละแถวของปิรามิด
    print(leading_spaces + line_string + leading_spaces)
