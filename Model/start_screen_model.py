import asyncio
import bleak
from bleak import BleakScanner
from asyncio import Task
from typing import Optional
from asyncio import AbstractEventLoop


class StartScreenModel:

    def __init__(self, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._observers = []
        self.scanned_devices = []

    def scanm(self) -> None:
        self._task = asyncio.create_task(self.task_scan())

    async def task_scan(self):
        self.scanned_devices = await BleakScanner.discover()
        print('Scanned devices: ', self.scanned_devices)
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
