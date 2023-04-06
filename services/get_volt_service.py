from overrides import override
from bleak import BleakClient
from services.get_volt_service_base import GetVoltServiceBase
from services.obr_fun import obr


class GetVoltService(GetVoltServiceBase):
    battery_voltage = 0
    rssi = 0

    def __init__(self, ble_device):
        self.device = ble_device
        self.client = BleakClient(self.device)

    async def client_con(self):
        print('2', self.client)
        await self.client.connect()

    @override
    async def get_volt(self):
        GetVoltService.battery_voltage = (
                str(obr(await self.client.read_gatt_char("964bfa71-51ae-49ff-98a8-b2f17c129716"))))

    async def discon1(self):
        await self.client.disconnect()