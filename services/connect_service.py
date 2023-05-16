from overrides import override
from bleak import BleakClient
from services.connect_service_base import ConnectServiceBase


class ConnectService(ConnectServiceBase):
    def __init__(self, ble_device):
        self.device = ble_device
        self.client = BleakClient(self.device)

    def bleak_client(self):
        return self.client

    @override
    async def connect(self):
        await self.client.connect()

    async def discon(self):
        await self.client.disconnect()