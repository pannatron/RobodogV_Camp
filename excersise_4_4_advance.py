# กำหนดลิสต์ของตัวเลข
List1 = [9, 10, 16, 2, 18, 21, 21, 31, 94, 101, 34, 1, 2, 30, 8, 19]

# หาค่าเฉลี่ยของลิสต์
average = sum(List1) / len(List1)

# นับสมาชิกที่มีค่าน้อยกว่าและมากกว่าค่าเฉลี่ย
below_average = sum(1 for x in List1 if x < average)
above_average = sum(1 for x in List1 if x > average)

# แสดงผลลัพธ์
print(f"mean is {average}")
print(f"Number of elements below average are {below_average}")
print(f"Number of elements above average are {above_average}")
