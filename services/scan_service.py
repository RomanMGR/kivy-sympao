from overrides import override
from bleak import BleakScanner
from services.scan_service_base import ScanServiceBase


class ScanService(ScanServiceBase):
    scanned_devices = []

    @override
    async def scan(self):
        ScanService.scanned_devices = await BleakScanner.discover()
        print(self.scanned_devices)
