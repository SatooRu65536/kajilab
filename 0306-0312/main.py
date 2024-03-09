import asyncio,logging
import bleak
from bleak import BleakClient

beacon_uuid = "FDA50693-A4E2-4fb1-AFCF-C6EB07647825"

def UUID_from_uuid(uuid):
    """
    To reconstruct the full 128-bit UUID from the shortened version, 
    insert the 16- or 32-bit short value (indicated by xxxxxxxx, 
    including leading zeros) into the Bluetooth Base UUID:
    xxxxxxxx-0000-1000-8000-00805F9B34FB
    """
    return f"{uuid:08x}-0000-1000-8000-00805f9b34fb"

# 定義済み　16bits UUID の幾つか
SYSTEM_ID_UUID = UUID_from_uuid(0x2A23)  # System ID
MODEL_NBR_UUID = UUID_from_uuid(0x2A24)  # Model Number String "00002a24-0000-1000-8000-00805f9b34fb"　
SER_NBR_UUID   = UUID_from_uuid(0x2A25)  # Serial Number String
FIRMW_REV_UUID = UUID_from_uuid(0x2A26)  # Firmware Revision String
HW_REV_UUID    = UUID_from_uuid(0x2A27)  # Hardware Revision String
SW_REV_UUID    = UUID_from_uuid(0x2A28)  # Software Revision String
MANU_NAME_UUID = UUID_from_uuid(0x2A29)  # Manufacturer Name String
REG_CERT_UUID  = UUID_from_uuid(0x2A2A)  # IEEE 11073-20601 Regulatory Certification Data List
CUR_TM_UUID    = UUID_from_uuid(0x2A2B)  # Current Time

async def main(address):
    async with BleakClient(address) as client:
        if not client.is_connected:
            await client.connect()
        model_number = await client.read_gatt_char(MODEL_NBR_UUID) 
        print("Model Number: {0}".format(model_number.decode('ascii'))) # Model Numberは文字列型
        try:
            serial_number = await client.read_gatt_char(SER_NBR_UUID) 
            print("Serial Number: {0}".format(serial_number.decode('ascii'))) 
        except bleak.BleakError as m:
            logging.warning(m)
        manufacture = await client.read_gatt_char(MANU_NAME_UUID) 
        print("Manufacture: {0}".format(manufacture.decode('utf-8'))) #

asyncio.run(main(beacon_uuid))
# await main(ipad_uuid)
