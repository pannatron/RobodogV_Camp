# Introduction to Bluetooth Communication with Python - Day 5
Welcome to Day 5 of our Python Programming Course! Today, we're venturing into the realm of wireless communication by using the Bleak library to connect and control devices over Bluetooth. Specifically, we will focus on interfacing with the Robodog Bittle, a small robot dog, using Python.

## Setting Up
Before we start interacting with the Robodog Bittle via Bluetooth, we need to install the Bleak library and prepare your environment:

### Install Bleak
Bleak is an asynchronous, cross-platform Bluetooth Low Energy (BLE) library for Python. It provides tools for discovering, connecting to, and interfacing with BLE devices. Install it using pip:

```bash
pip install bleak
```

### Clone the Course Repository
If not already done, clone the course repository to access today's instructional content:
```bash
git clone https://github.com/pannatron/RobodogV_Camp.git
cd RobodogV_Camp
git checkout day5
```
## Day 5 Exercises Overview
In today's session, we'll cover:

 - Bluetooth Basics and BLE Introduction: Understanding how Bluetooth and BLE work.
 - Discovering Devices: How to use Bleak to find BLE devices around you, including the Robodog Bittle.
 - Connecting to the Robodog Bittle: Steps to establish a BLE connection with the Robodog Bittle.
 - Controlling the Robodog Bittle: Sending commands to perform various actions.
 - Bluetooth Communication Techniques
### 1. Bluetooth Basics and BLE Introduction
Learn the fundamentals of Bluetooth and Bluetooth Low Energy (BLE), which is crucial for efficient, low-power device communication.
### 2.Discovering Devices
Scan for available BLE devices using Bleak. Here's a basic script to list all nearby BLE devices:
```bash

import asyncio
from bleak import BleakScanner

async def scan():
    devices = await BleakScanner.discover()
    for device in devices:
        print(device)

loop = asyncio.get_event_loop()
loop.run_until_complete(scan())
```
### 3. Connecting to the Robodog Bittle
To connect to the Robodog Bittle, you'll need to identify it by its unique BLE address or name. Here’s how you can establish a connection:
```bash
import asyncio
from bleak import BleakClient

address = "BLE_DEVICE_ADDRESS"  # Replace with your Robodog Bittle's BLE address
async def connect():
    async with BleakClient(address) as client:
        is_connected = await client.is_connected()
        print(f"Connected: {is_connected}")

loop = asyncio.get_event_loop()
loop.run_until_complete(connect())
```


