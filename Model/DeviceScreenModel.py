import asyncio
import bleak
from asyncio import Task
from asyncio import AbstractEventLoop
from typing import Optional
from services.get_volt_service import GetVoltService
from bleak import BleakClient


class DeviceScreenModel:

    lb_battery_voltage = 0
    rssi = 0
    examp_class_serv = ''

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._loop: AbstractEventLoop = loop
        self._observers = []
        self.screen_transition_service = screen_transition_service
        self.__mac = None
        self.__device = None
        self.__name = None

    def start(self, device, mac, name):
        self.__mac = mac
        self.__device = device
        self.__name = name
        self.check_volt()

    def get_name(self):
        return self.__name

    def check_volt(self):
        self._task = self._loop.create_task(self.task_volt())

    async def task_volt(self):
        self.examp_class_serv = GetVoltService(self.__device)
        await self.examp_class_serv.client_con()
        while True:
            try:
                await self.examp_class_serv.get_volt()
                DeviceScreenModel.lb_battery_voltage = GetVoltService.battery_voltage
                print(DeviceScreenModel.lb_battery_voltage)
                self.notify_observers()
                await asyncio.sleep(5)
            except bleak.exc.BleakError as e:
                print('error')

    def discon(self):
        self._task.cancel()
        self._task = self._loop.create_task(self.task_discon())

    async def task_discon(self):
        await self.examp_class_serv.discon1()

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
