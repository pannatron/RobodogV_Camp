# กำหนด tuple ของตัวเลข
tuple1 = (1, 2, 3, 4, 5, 6)

# หาผลรวมขององค์ประกอบใน tuple
total_sum = sum(tuple1)

# สร้าง tuple ใหม่ที่มีผลรวมอยู่ที่ดัชนีแรก
new_tuple = (total_sum,) + tuple1  # (total_sum,) เป็นการสร้าง tuple จากผลรวม

# แสดงผลลัพธ์
print(new_tuple)
