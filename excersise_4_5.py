# กำหนดลิสต์ของตัวเลข
List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# แปลงลิสต์เป็นสตริงรูปแบบเบอร์โทรศัพท์
# ตัวแปรสำหรับจัดเก็บสตริงรูปแบบเบอร์โทรศัพท์
phone_number_format = "(" + str(List1[0]) + str(List1[1]) + str(List1[2]) + ") " + \
                      str(List1[3]) + str(List1[4]) + str(List1[5]) + "-" + \
                      str(List1[6]) + str(List1[7]) + str(List1[8]) + str(List1[9])

# แสดงผลลัพธ์
print(phone_number_format)
