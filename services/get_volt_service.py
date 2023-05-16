from overrides import override
from bleak import BleakClient
from services.get_volt_service_base import GetVoltServiceBase
from services.obr_fun import obr


class GetVoltService(GetVoltServiceBase):
    battery_voltage = 0
    rssi = 0

    @override
    async def get_volt(self, ble_client):
        GetVoltService.battery_voltage = (
                str(obr(await ble_client.read_gatt_char("964bfa71-51ae-49ff-98a8-b2f17c129716"))))
