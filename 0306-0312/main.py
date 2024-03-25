import asyncio
from bleak import BleakScanner
from bleak.uuids import normalize_uuid_str


def on_advertisement_received(device, advertisement_data):
    value = advertisement_data.service_data.values()
    for v in value:
        print(v)


async def start_scan():
    ble_scanner = BleakScanner(on_advertisement_received)

    await ble_scanner.start()
    while True:
        await asyncio.sleep(1.0)


asyncio.run(start_scan())
