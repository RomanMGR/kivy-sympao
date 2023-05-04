from overrides import override
from services.send_parameters_service_base import SendParametersServiceBase



class SendParametersService(SendParametersServiceBase):

    @override
    async def send_anode(self, ble_client, n):
        a = await ble_client.write_gatt_char(char_specifier="6c193878-7b97-4281-b29e-7ab92b36a2ff", data=hex(n)[2:])
        print(n,' 16=',  a)

    async def send_amp(self, ble_client, value):
        print('send amP!!!!!!')
        b = await ble_client.write_gatt_char(char_specifier="e48b1dd8-19cb-474f-8c34-8ea752fdf683", data=hex(int(value*100))[2:])
        print('amp!!!!!!=',  value)

    async def send_dlit(self, ble_client, value):
        c = await ble_client.write_gatt_char(char_specifier="6a03a595-7bc7-4abe-8d68-c116489fcc45", data=hex(int(value*8))[2:])
        print('dlit=',  value)

    async def send_chast(self, ble_client, value):
        d = await ble_client.write_gatt_char(char_specifier="8bfdff2c-894f-4f9e-bb0a-86838de384e2",
                                             data=hex(int(1000/value*6557/200))[2:])
        print('chast=',  value)

    async def send_segment(self,ble_client, n):
        e = await ble_client.write_gatt_char(char_specifier="c4f1cde1-03fa-4577-843e-f5fd12036704",
                                             data=hex(int(n))[2:])
        print('segment=', n)
