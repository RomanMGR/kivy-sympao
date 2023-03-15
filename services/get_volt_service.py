import bleak
import asyncio
from overrides import override
from bleak import BleakClient
from services.get_volt_service_base import GetVoltServiceBase


class GetVoltService(GetVoltServiceBase):
    battery_voltage = 0

    def __init__(self, device) -> None:
        self.device = device
        self.client = BleakClient(self.device)

    async def client_con(self):
        await self.client.connect()

    @override
    async def get_volt(self):
        print('GetVolt -- --',self.client)
        GetVoltService.battery_voltage = (
                str(obr(await self.client.read_gatt_char("964bfa71-51ae-49ff-98a8-b2f17c129716"))))

    async def discon(self):
        await self.client.disconnect()
        print('service discon called')


def obr(read_ch):
    if len(read_ch) > 2:
        read_ch = int(read_ch[1:], 16)
    else:
        read_ch = int(read_ch)
    return read_ch