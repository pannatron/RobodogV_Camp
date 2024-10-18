import asyncio
from bleak import BleakClient

uuid = "661B09E8-8866-A3E9-F1EE-0008208263E7"
characteristic_uuid_notify = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # UUID สำหรับรับการแจ้งเตือน
characteristic_uuid_write = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # UUID สำหรับส่งคำสั่ง

# ตัวนับสำหรับการเช็คข้อมูล rc
rc_count = 0

# Callback function ที่จะถูกเรียกเมื่อได้รับการแจ้งเตือน
def notification_handler(sender, data):
    global rc_count
    print(f"ข้อมูลที่ได้รับจาก {sender}: {data}")
    
    # แปลงข้อมูลเป็น string เพื่อเปรียบเทียบ
    if data == bytearray(b'rc'):
        rc_count += 1
        print(f"ข้อมูลที่ได้รับคือ 'rc', นับจำนวนครั้งที่ {rc_count}")
        
        # ถ้าได้รับ 'rc' ครบ 3 ครั้ง
        if rc_count >= 3:
            print("game over")
            rc_count = 0  # รีเซ็ตตัวนับเพื่อเตรียมสำหรับรอบต่อไป
            asyncio.create_task(send_kbalance())  # เรียกใช้ฟังก์ชันส่งคำสั่ง kbalance
    else:
        print("ข้อมูลที่ได้รับไม่ใช่ 'rc'")

# ฟังก์ชันส่งคำสั่ง kbalance หลังจาก game over
async def send_kbalance():
    await asyncio.sleep(3)  # รอ 3 วินาที
    print("ส่งคำสั่ง 'kbalance' ไปยัง Petoi")
    await client.write_gatt_char(characteristic_uuid_write, b'kbalance')

async def send_command_once(client):
    command = b"ksit"
    await client.write_gatt_char(characteristic_uuid_write, command)
    print(f"ส่งคำสั่ง: {command}")

async def read_from_petoi():
    global client
    async with BleakClient(uuid) as client:
        if client.is_connected:
            print("เชื่อมต่อกับ Petoi สำเร็จ")
            try:
                # รอ 3 วินาทีหลังจากเชื่อมต่อ
                await asyncio.sleep(3)

                # ส่งคำสั่ง "ksit" ครั้งเดียว
                await send_command_once(client)

                # สมัครรับการแจ้งเตือน
                await client.start_notify(characteristic_uuid_notify, notification_handler)

                # วนลูปรอรับการแจ้งเตือนทุกๆ 1 วินาที
                while True:
                    await asyncio.sleep(1)  # รอ 1 วินาทีก่อนอ่านใหม่

            except Exception as e:
                print(f"เกิดข้อผิดพลาด: {e}")
            finally:
                # หยุดการรับการแจ้งเตือนเมื่อโปรแกรมจบ
                await client.stop_notify(characteristic_uuid_notify)
        else:
            print("ไม่สามารถเชื่อมต่อกับ Petoi")

asyncio.run(read_from_petoi())
