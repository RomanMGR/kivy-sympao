import asyncio
import bleak
from asyncio import Task
from typing import Optional
from bleak import BleakClient
from asyncio import AbstractEventLoop

from services.get_volt_service import GetVoltService


class DeviceScreenModel:

    device = ''
    lb_battery_voltage = 0
    services = ''

    def __init__(self, loop:AbstractEventLoop, **kwargs) -> None:
        self._loop: AbstractEventLoop = loop
        self._task: Optional[Task] = None
        self._observers = []

    def check_volt(self):
        print('111111111')
        self._task = asyncio.create_task(self.task_volt())

    async def task_volt(self):
        print('MAC = ', self.device)
        self.services = GetVoltService(self.device)
        await self.services.client_con()
        while True:
            try:
                await self.services.get_volt()
                DeviceScreenModel.lb_battery_voltage = GetVoltService.battery_voltage
                print(DeviceScreenModel.lb_battery_voltage)
                self.notify_observers()
                await asyncio.sleep(5)
            except bleak.exc.BleakError as e:
                print('error')

    def discon(self):
        asyncio.Task.cancel(self._task)
        self._task = asyncio.create_task(self.task_discon())
        print('def discon called')

    async def task_discon(self):
        print('do task dicon')
        await self.services.discon()
        print('def TASK discon called')

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
