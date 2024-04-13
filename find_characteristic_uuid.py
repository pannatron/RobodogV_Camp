import asyncio
from bleak import BleakClient

uuid = "EA9EA3F3-42F7-4037-142D-FBD1FC4962B3"

async def discover_services_and_characteristics():
    async with BleakClient(uuid) as client:
        if client.is_connected:
            print("เชื่อมต่อกับ Petoi สำเร็จ")
            for service in client.services:
                print(f"Service: {service.uuid}")
                for char in service.characteristics:
                    print(f"  Characteristic: {char.uuid}, (Handle: {char.handle})")
        else:
            print("ไม่สามารถเชื่อมต่อกับ Petoi")

asyncio.run(discover_services_and_characteristics())
