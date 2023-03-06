import asyncio
import bleak
from bleak import BleakScanner
from asyncio import Task
from typing import Optional
from bleak import BleakClient


class DeviceScreenModel:
    MAC = ''
    lb_battery_voltage = 0

    def __init__(self, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._observers = []

    def check_volt(self):
        print('111111111')
        self._task = asyncio.create_task(self.task_volt())

    async def task_volt(self):
        print('MAC = ', DeviceScreenModel.MAC)
        while True:
            try:
                async with BleakClient(DeviceScreenModel.MAC) as client:
                    battery_voltage = (str(obr(await client.read_gatt_char("964bfa71-51ae-49ff-98a8-b2f17c129716"))))
                    print(battery_voltage)
                    DeviceScreenModel.lb_battery_voltage = battery_voltage
                    self.notify_observers()
                    await asyncio.sleep(5)
            except bleak.exc.BleakError as e:
                print('error')

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)


def obr(read_ch):
    if len(read_ch) > 2:
        read_ch = int(read_ch[1:], 16)
    else:
        read_ch = int(read_ch)
    return read_ch


# def mac(mac):
#     print('obrab mac:',mac)
#     MAC = mac


