from services.scan_service import ScanService
from asyncio import Task
from typing import Optional
from asyncio import AbstractEventLoop


class StartScreenModel:

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._loop: AbstractEventLoop = loop
        self._observers = []
        self.scanned_devices = []
        self.screen_transition_service = screen_transition_service

    def scanm(self) -> None:
        self._task = self._loop.create_task(self.task_scan())

    async def task_scan(self):
        await ScanService().scan()
        self.scanned_devices = ScanService.scanned_devices
        self.notify_observers()

    def on_device_connect_taped(self, device, mac, name):
        self.screen_transition_service.connect_to_device(device, mac, name)

    def show_menu(self, name):
        self.screen_transition_service.show_menu(name)

    def start_n(self):
        self.screen_transition_service.start_n()

    def start_corsi(self):
        self.screen_transition_service.start_corsi()

    def start_results(self):
        self.screen_transition_service.start_results()

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
