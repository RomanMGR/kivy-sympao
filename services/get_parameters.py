from overrides import override
from bleak import BleakClient
from services.get_parameters_base import GetParametersServiceBase
from services.obr_fun import obr


class GetParametersService(GetParametersServiceBase):

    @override
    async def get_parameters(self, ble_client):
        amplitude = str((obr(await ble_client.read_gatt_char("a38caad7-2f1e-4b64-8028-3aca28b28f51")))*25/2500)
        print('amplitude', amplitude)
        impulse_width = str(obr(await ble_client.read_gatt_char("93fb864e-0c35-4a3b-8dcd-59fa47c6d11b"))*60/480)
        print('impulse', impulse_width)
        packet_width = (obr(await ble_client.read_gatt_char("dc210dd3-c32c-4ea6-a874-1b3c706d7a6e")))*200/6557
        packet_grc = str(1000/packet_width)
        print('package', packet_grc)
        anode = str(obr(await ble_client.read_gatt_char("9f52cac2-986a-4a52-b8c2-dea5381cfe11")))
        print('anode', anode)
        state = str(obr(await ble_client.read_gatt_char("32845da2-9cc8-4bfb-b086-35b1fee0d65e")))
        print('state', state)
        return [amplitude, impulse_width, packet_grc, anode, state]
