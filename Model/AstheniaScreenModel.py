from asyncio import Task
from typing import Optional
from asyncio import AbstractEventLoop
from services.export_data import ExportData


class AstheniaScreenModel:

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._loop: AbstractEventLoop = loop
        self._observers = []
        self.screen_transition_service = screen_transition_service
        self.export_data = ExportData()

    def choose(self, btn, n, current_screen):
        self.screen_transition_service.count_asthenia(n, current_screen)
        self.export_data.react_time_pos(n)
        self.notify_observers()

    def send_data(self, export, comment, count_list):
        uuid = self.screen_transition_service.get_uuid()
        self.screen_transition_service.save_data_asthenia(comment)
        self.export_data.send_asthenia(export, uuid, count_list)

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)