# กำหนดลิสต์ของตัวเลข
List1 = [9, 10, 16, 2, 18, 21, 21, 31, 94, 101, 34, 1, 2, 30, 8, 19]

# คำนวณค่าเฉลี่ยของลิสต์
total_sum = sum(List1)  # หาผลรวมของสมาชิกในลิสต์
number_of_elements = len(List1)  # นับจำนวนสมาชิกในลิสต์
average = total_sum / number_of_elements  # คำนวณค่าเฉลี่ย

# นับจำนวนสมาชิกที่มีค่าน้อยกว่าค่าเฉลี่ย
below_average_count = 0  # ตั้งตัวนับจำนวนสมาชิกที่น้อยกว่าค่าเฉลี่ย
for element in List1:
    if element < average:
        below_average_count += 1

# นับจำนวนสมาชิกที่มีค่ามากกว่าค่าเฉลี่ย
above_average_count = 0  # ตั้งตัวนับจำนวนสมาชิกที่มากกว่าค่าเฉลี่ย
for element in List1:
    if element > average:
        above_average_count += 1

# แสดงผลลัพธ์
print(f"mean is {average}")
print(f"Number of elements below average are {below_average_count}")
print(f"Number of elements above average are {above_average_count}")
