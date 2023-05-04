import asyncio
import bleak
from asyncio import Task
from asyncio import AbstractEventLoop
from typing import Optional


class NbackScreenModel:

    def __init__(self, screen_transition_service, loop, **kwargs) -> None:
        self._task: Optional[Task] = None
        self._loop: AbstractEventLoop = loop
        self._observers = []
        self.screen_transition_service = screen_transition_service

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def show_menu(self):
        self.screen_transition_service.show_menu()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
