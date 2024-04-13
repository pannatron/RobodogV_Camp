import asyncio
from bleak import BleakClient

uuid = "EA9EA3F3-42F7-4037-142D-FBD1FC4962B3"
characteristic_uuid = "0000ffe2-0000-1000-8000-00805f9b34fb"

async def send_command_to_petoi():
    async with BleakClient(uuid) as client:
        if client.is_connected:
            print("เชื่อมต่อกับ Petoi สำเร็จ")
            try:
                # ตัวอย่างของการพิมพ์ค่าที่จะส่ง
                command = b"ksit"
                print(f"กำลังส่งคำสั่ง: {command}")
                
                # ใช้ asyncio.sleep แทน time.sleep
                await asyncio.sleep(10)
                await client.write_gatt_char(characteristic_uuid, command)
                print("ส่งคำสั่ง 'ksit' ไปยัง Petoi")
                
    
                command = b"kbx"
                await asyncio.sleep(3)
                await client.write_gatt_char(characteristic_uuid, command)
                
                command = b"kjmp"
                await asyncio.sleep(8)
                await client.write_gatt_char(characteristic_uuid, command)

                command = b"kvtLX"
                await asyncio.sleep(5)
                await client.write_gatt_char(characteristic_uuid, command)

            except Exception as e:
                print(f"เกิดข้อผิดพลาด: {e}")
        else:
            print("ไม่สามารถเชื่อมต่อกับ Petoi")

asyncio.run(send_command_to_petoi())
